from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from .models import Photo
from django.conf.urls import url

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/photo_detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    url(r'^photo/(?P<pk>\d+)/comment/$', add_comment_to_photo, name='add_comment_to_photo'),
]
