from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('' , views.HomeView.as_view() , name='home'),
    path('bucket/' , views.BucketView.as_view() , name='bucket'),
    path('bucket_obj_del/<key>' , views.Delete_obj_BucketView.as_view() , name='bucket_del_obj'),
    path('<slug:slug>/' , views.ProductDetailView.as_view() , name='detail_view'),
]