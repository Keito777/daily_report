from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

#signup
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import LoginForm, SignupForm
from django.shortcuts import redirect
from django.urls import reverse_lazy

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/logout.html'
# ログアウト後は、LOGOUT_REDIRECT_URL = 'products:login'にリダイレクトするため、ログアウト用のHTMLは空でもいい


'''サインアップ'''
class Signup(CreateView):
    template_name = 'accounts/signup.html'
    form_class =SignupForm
    success_url = reverse_lazy('accounts:signup_success')

    # templateに表示するデータを追加するためオーバーライド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

    '''定義されているためオーバーライド不要
    def form_valid(self, form):
        user = form.save() # formの情報を保存
        self.object = user
        return super().form_valid(form)
    '''

'''サインアップ完了'''
class SignupDone(TemplateView):
    template_name = 'accounts/signup_success.html'