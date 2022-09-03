from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

class Index(LoginRequiredMixin, ListView):
    template_name = 'report/index.html'
    model = Post
    ordering = 'created' # 新規作成順　'-createdで降順'
    

class Detail(LoginRequiredMixin, DetailView):
    template_name = 'report/detaile.html'
    model = Post


class Create(LoginRequiredMixin, CreateView):
    template_name = 'report/create.html'
    model = Post # form_classは記述が多くなるのでmodelを使用
    fields = ['title', 'body']

    # idパラメータも渡す
    def get_success_url(self):
        return reverse('report:detail', kwargs={'pk': self.object.id})


class Update(LoginRequiredMixin, UpdateView):
    template_name = 'report/create.html'
    model = Post
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('report:detail', kwargs={'pk': self.object.id})

class Delete(LoginRequiredMixin, DeleteView):
    template_name = 'report/delete.html'
    model = Post
    def get_success_url(self):
        return reverse('report:index')