from django.urls import path
from .views import Login, Logout, Signup, SignupDone

app_name = 'accounts'

urlpatterns = [
    # accounts
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Signup.as_view(), name='signup'), # サインアップ
    path('signup_done/', SignupDone.as_view(), name='signup_success'), # サインアップ完了
    #path('signup/', account_views.SignUp.as_view(), name='signup'),
    #path('accounts/', account_views.AccountList.as_view(), name='account_list'),
    #path('accounts/edit/<int:pk>', account_views.AccountEdit.as_view(), name='account_edit'),
    #path('accounts/delete/<int:pk>', account_views.account_delete, name='account_delete')
]