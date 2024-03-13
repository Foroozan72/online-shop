from django.urls import path , include
from . import views

app_name = 'home'

bucket_urls = [
	path('', views.BucketView.as_view(), name='bucket'),
	path('obj_del/<key>' , views.Delete_obj_BucketView.as_view() , name='bucket_del_obj'),
	path('download_obj/<str:key>/', views.DownloadBucketObject.as_view(), name='download_obj_bucket'),
]

urlpatterns = [
    path('' , views.HomeView.as_view() , name='home'),
    path('bucket/', include(bucket_urls)),
    path('bucket_obj_del/<key>' , views.Delete_obj_BucketView.as_view() , name='bucket_del_obj'),
    path('<slug:slug>/' , views.ProductDetailView.as_view() , name='detail_view'),
]