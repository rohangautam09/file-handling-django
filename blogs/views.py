from django.shortcuts import render,redirect,get_object_or_404
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

def viewblog(request,blog_id):
	blog = get_object_or_404(Blog,pk=blog_id)
	# blog = Blog.objects.all()
	return render(request,'blogs/viewblog.html',{'blog':blog})









# Create your views here.
