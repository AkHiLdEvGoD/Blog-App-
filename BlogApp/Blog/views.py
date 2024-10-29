from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from .forms import BlogForm
# Create your views here.

def home(request):
    return render(request,'./home.html')

def BlogSite(request):
    blogs = Blog.objects.all().order_by('-time_date_posted')
    return render(request,'Blog/blogSite.html',{'blogs':blogs})

def BlogDetail(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    return render(request,'Blog/blogDetail.html',{'blog':blog})

@login_required
def BlogCreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('list')
    else:
        form = BlogForm()
    return render(request,'Blog/blogForm.html',{'form':form})

@login_required
def BlogEdit(request,pk):
    blog = get_object_or_404(Blog,pk=pk,user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your blog post has been updated!')
            return redirect('detail',pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request,'Blog/blogForm.html',{'form':form})

@login_required
def BlogDelete(request,pk):
    blog = get_object_or_404(Blog,pk=pk,user=request.user)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Your blog post has been updated!')
        return redirect('detail',pk=blog.pk)
    return render(request,'Blog/blogConfirmDelete.html',{'blog':blog})