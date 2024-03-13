from django.shortcuts import render , redirect
from django.views import View
from .models import Product
from django.shortcuts import get_object_or_404 
from . import tasks
from django.contrib import messages



# Create your views here.

class HomeView(View):

    def get(self, request):
        products = Product.objects.filter(available = True)
        return render(request , 'home/home.html' , {'products':products})
    

class ProductDetailView(View):
    def get(self , request , slug ):
        product = get_object_or_404(Product , slug=slug)
        return render(request , 'home/detail.html' , {'product':product})
    

class BucketView(View):
        template_name = 'home/bucket.html'
        def get(self, request):
            objects = tasks.all_bucket_objects_task()
            print(objects)
            return render(request , self.template_name , {'objects' : objects} )


class Delete_obj_BucketView(View):
     
     def get(self,request ,key):
          tasks.delete_object_task.delay(key)
          messages.success(request , 'your object delete after a wihle')
          return redirect('home:bucket')


class DownloadBucketObject(View):
	def get(self, request, key):
		tasks.download_object_task.delay(key)
		messages.success(request, 'your download will start soon.', 'info')
		return redirect('home:bucket')

          
