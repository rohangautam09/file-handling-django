from django.shortcuts import render,redirect
from .models import Blog
from django.core.files.storage import FileSystemStorage
from . forms import BlogForm

def home(request):
	blog = Blog.objects.all()
	return render(request,'blogs/home.html',{'blog':blog})

def addblog(request):
	if request.method == 'POST':
		form = BlogForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = BlogForm()
	return render(request,'blogs/addblog.html',{'form':form})









# Create your views here.
