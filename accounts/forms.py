from django.contrib.auth.forms import AuthenticationForm 

class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

'''
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from products.models import User, Locale

class UploadFileForm(forms.Form):
    file = forms.FileField()


class LoginForm(AuthenticationForm): # ログインフォームを実装（AuthenticationFormを継承することによって）
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-cmn-input-01' # フィールドのウィジェットを設定
            field.widget.attrs['placeholder'] = field.label # フィールドのウィジェットを設定


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    is_staff = forms.ChoiceField(label='管理者権限', required=True, widget=forms.RadioSelect, choices=((True, 'Administrator'), (False, 'Editor')), initial=True)
    locales = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': "list-checkbox-01-signup"}), to_field_name='slug', label='locale', required=False, queryset=Locale.objects.all())
    # password1 = forms.~
    # password2 = forms.~

    def clean_locales(self):
        is_staff = self.cleaned_data["is_staff"]
        locales = self.cleaned_data["locales"]
        if is_staff == "False" and not locales:
            raise forms.ValidationError('Editor users are required to select locales.')

        return locales

    class Meta:
        # model:指定したモデルで定義されている全フィールドを自動で定義する（自動生成）
        model = User
        # fields:
        # modelで指定したモデルの、どのフィールドをテンプレート上に表示するかを指定する。（モデルのフィールド名を指定する）
        # つまり、指定したフィールドは、ユーザからの入力を受け付けるため、入力値がモデルに保存される
        # is_staff, password1, passwor2は、独自に定義したフォームであるためここに書かないこと（混乱の原因）
            # モデルに保存する値かどうかを直感的に判断できなくなる
        # モデルから自動定義したフィールドも独自に定義したフィールドも{{form}}によってテンプレートに表示できる
        fields = ('username', 'email', 'is_staff', 'locales', 'password1', 'password2')


class AccountUpdateForm(SignUpForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
        required=False
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        required=False
    )

    # save()メソッドをオーバーライド
    # cleaned_data：バリデーションに成功したフィールドのみを格納している
 
    def save(self, commit=True):
        user = super().save(commit=False) # Falseによって、DBにまだ保存されていない入力値を取得
        if self.cleaned_data["password1"] == "":
            if commit:
                user.save(update_fields=['username', 'email', 'is_staff'])
        else:
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
        return user
'''