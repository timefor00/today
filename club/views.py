from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView, ListView, DetailView
from club.forms import PersonInfoForm, ReservationCancel
from club.models import ReservationDate, PersonInfo
from django.db import connection
import string
import random


class IndexView(TemplateView):
    template_name = 'index.html'


class ReservationView(ListView):
    template_name = 'reservation.html'
    model = ReservationDate
    context_object_name = 'reservation_date'


class ReservationTimeView(DetailView,FormView):
    template_name = 'reservationtimes.html'
    model = ReservationDate
    queryset = ReservationDate.objects.all()
    form_class = PersonInfoForm
    success_url = '../../reservation_complete'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super(ReservationTimeView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def form_valid(self,form):
        person_info = form.cleaned_data

        reservation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) # generate random code
        try:
            reservation_id = PersonInfo.objects.latest('reservation_id').reservation_id + 1 # get first empty pk
        except: # if database is empty, then set 1
            reservation_id = 1
        #save person
        person_model_make = PersonInfo( reservation_id = reservation_id,
                                        first_name = person_info['first_name'],
                                        sur_name = person_info['sur_name'],
                                        email = person_info['email'],
                                        mobil_phone = person_info['mobil_phone'],
                                        reservation_code =  reservation_code,
                                        date_id = self.kwargs['pk'])

        person_model_make.save()
        #reserve term in database
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE club_ReservationDate SET {person_info['Time_Select']} = {reservation_id} WHERE day_id = {self.kwargs['pk']}")

        # send email with code

        return render(self.request,'reservation_complete.html',{'code':reservation_code})


class ReservationCompleteView(TemplateView):
    template_name = 'reservation_complete.html'


class ReservationCancelView(TemplateView,FormView):
    template_name = 'reservation_cancel.html'
    form_class = ReservationCancel
    success_url = "../"


    def form_valid(self, form):
        info = form.cleaned_data
        try:
            ids_info = PersonInfo.objects.filter(reservation_code = info['your_code'],email = info['your_email']).values('date_id','reservation_id')[0]# get date info
        except:
            print(form)
            return render(self.request,self.template_name,{'form':form,
                                                            'message':'Your code or email is wrong, please try again or call our support'})

        date_times = ReservationDate.objects.filter(day_id=ids_info['date_id']).values()[0]
        # looking for reserved time
        for key in date_times.keys():
            if date_times[key] == str(ids_info['reservation_id']):
                time_to_change = key

        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE club_ReservationDate SET {time_to_change} = 'open' WHERE day_id = {ids_info['date_id']}") # set default value

            cursor.execute(f"DELETE FROM club_PersonInfo WHERE reservation_id = '{ids_info['reservation_id']}'") # delete person
        return super().form_valid(form)

