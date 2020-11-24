from django import forms
from club.models import PersonInfo, ReservationDate


class ReservationCancel(forms.Form):

    your_code = forms.CharField(max_length=10)
    your_email = forms.EmailField(max_length=30)


class ContactForm(forms.Form):

    sur_name = forms.CharField(max_length = 70)
    last_name = forms.CharField(max_length = 70)
    your_email = forms.EmailField(max_length = 70)
    subject = forms.CharField(max_length = 50)
    message = forms.CharField(max_length = 400,widget=forms.Textarea)


class PersonInfoForm(forms.ModelForm):
    #dynamic field
    def __init__(self,pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get day info
        hours = list(ReservationDate.objects.filter(day_id=pk).values())[0]

        # display not reserved hours in dropdown box
        free_hours = []
        for key in hours.keys():
            if  key == 'T10_11'and hours[key] == 'open':
                free_hours.append((key,'10:00-11:00'))
            elif key == 'T11_12'and hours[key] == 'open':
                free_hours.append((key,'11:00-12:00'))
            elif key == 'T12_13'and hours[key] == 'open':
                free_hours.append((key,'12:00-13:00'))
            elif key == 'T13_14'and hours[key] == 'open':
                free_hours.append((key,'13:00-14:00'))
            elif key == 'T14_15'and hours[key] == 'open':
                free_hours.append((key,'14:00-15:00'))
            elif key == 'T15_16'and hours[key] == 'open':
                free_hours.append((key,'15:00-16:00'))
            elif key == 'T16_17'and hours[key] == 'open':
                free_hours.append((key,'16:00-17:00'))
            elif key == 'T17_18'and hours[key] == 'open':
                free_hours.append((key,'17:00-18:00'))
            elif key == 'T18_19'and hours[key] == 'open':
                free_hours.append((key,'18:00-19:00'))
            elif key == 'T19_20'and hours[key] == 'open':
                free_hours.append((key,'19:00-20:00'))
            elif key == 'T20_21'and hours[key] == 'open':
                free_hours.append((key,'20:00-21:00'))

        self.fields['Time_Select'] = forms.ChoiceField(choices = free_hours)

    class Meta:
        model = PersonInfo
        fields = ['first_name','sur_name','email','mobil_phone']


class JoinUsForm(forms.Form):
    sur_name = forms.CharField(max_length = 70,)
    last_name = forms.CharField(max_length = 70)
    your_email = forms.EmailField(max_length = 70)
    subject = forms.CharField(max_length = 50)
    message = forms.CharField(max_length = 400,widget=forms.Textarea)
    file = forms.FileField()