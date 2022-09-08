from django.urls import path
from .views import Login, Logout, Signup, SignupDone, MyPage,UserUpdate, PasswordChange, PasswordChangeDone

app_name = 'accounts'

urlpatterns = [
    # accounts
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    
    path('signup/', Signup.as_view(), name='signup'), # サインアップ
    path('signup_done/', SignupDone.as_view(), name='signup_success'), # サインアップ完了

    path('my_page/<int:pk>/', MyPage.as_view(), name='my_page'), # 追加
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'), # 登録情報の更新

    path('password_change/', PasswordChange.as_view(), name='password_change'), # パスワード変更
    path('password_change_done/', PasswordChangeDone.as_view(), name='password_change_done'), # パスワード変更完了
    #path('signup/', account_views.SignUp.as_view(), name='signup'),
    #path('accounts/', account_views.AccountList.as_view(), name='account_list'),
    #path('accounts/edit/<int:pk>', account_views.AccountEdit.as_view(), name='account_edit'),
    #path('accounts/delete/<int:pk>', account_views.account_delete, name='account_delete')
]