from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import Post
from .forms import BlogForm

# Create your views here.
def index (request):
    posts = Post.objects.all()
    args = {"posts": posts}
    return render(request, "blog/index.html", args)

def create (request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
    else:
        form = BlogForm()
        args = {"form": form}
        return render(request,"blog/blog_form.html",args)