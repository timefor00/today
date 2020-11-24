from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'today'

urlpatterns = [
    path('', studio_home, name='studio_home'),
    path('today/', product_in_category, name='product_all'),
    path('today/<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('today/<int:id>/<product_slug>/', product_detail, name='product_detail'),
    path('upload/', ReviewUploadView.as_view(), name='review_upload'),
    path('reveiw/<int:pk>/', DetailView.as_view(model=Review, template_name='today/review.html'), name='review_detail'),
]
