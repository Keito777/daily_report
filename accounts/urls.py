from django.urls import path
from .views import Login, Logout

app_name = 'accounts'

urlpatterns = [
    # accounts
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    #path('signup/', account_views.SignUp.as_view(), name='signup'),
    #path('accounts/', account_views.AccountList.as_view(), name='account_list'),
    #path('accounts/edit/<int:pk>', account_views.AccountEdit.as_view(), name='account_edit'),
    #path('accounts/delete/<int:pk>', account_views.account_delete, name='account_delete')
]