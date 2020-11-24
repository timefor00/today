from django.urls import path

from . import views
from .views import ReservationView, ReservationCompleteView, ReservationCancelView

app_name = 'club'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('reservation', ReservationView.as_view(), name='reservation'),
    path('reservation/<int:pk>/', views.ReservationTimeView.as_view(), name='Reservation-times'),
    path('reservation_complete', ReservationCompleteView.as_view(), name='Reservation-complete'),
    path('reservation/cancel', ReservationCancelView.as_view(), name='Reservation-cancel'),

]