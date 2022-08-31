from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

class Index(ListView):
    template_name = 'index.html'
    model = Post

class Detail(DetailView):
    template_name = 'detaile.html'
    model = Post