from django.shortcuts import render

# Create your views here.

# CBVs  https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from . models import Post


#logic with classes

class PostList(ListView) :
    model = Post


class PostDetail(DetailView) :
     model = Post

class PostCreate() :
    pass

class PostDelete() :
    pass

class PostUpdate() :
    pass
