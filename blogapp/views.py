from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BlogModel
from django.urls import reverse, reverse_lazy

class Bloglist(ListView):
    template_name = ('list.html')
    model = BlogModel

class Blogdetail(DetailView):
    template_name = ('detail.html')
    model = BlogModel

class Blogcreate(CreateView):
    template_name = ('create.html')
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

class Blogdelete(DeleteView):
    template_name = ('delete.html')
    model = BlogModel
    success_url = reverse_lazy('list')

class Blogupdate(UpdateView):
    template_name = ('update.html')
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')