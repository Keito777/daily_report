from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.urls import reverse_lazy

from .models import Post

class Index(ListView):
    template_name = 'index.html'
    model = Post

class Detail(DetailView):
    template_name = 'detaile.html'
    model = Post


class Create(CreateView):
    template_name = 'create.html'
    model = Post # form_classは記述が多くなるのでmodelを使用
    fields = ['title', 'body']

    # idパラメータも渡す
    def get_success_url(self):
        #return reverse('report:index') これでもリダイレクトされない
        return reverse('report:detail', kwargs={'pk': self.object.id})
        # おそらくself.objectはNoneなので、リダイレクトされない