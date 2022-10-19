'''
settings.py内の全ての環境変数を読み込み、DEBUG, ALLOWED_HOSTS, DATABASESをオーバーライド
※importしたモジュール（Path, load_dotenvなど）も含まれる
'''
from .settings import *
from django.contrib import messages

DEBUG = True
ALLOWED_HOSTS = ['*']

#開発環境用のDB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# フォーム入力時、値に応じてログを表示する
MESSAGE_TAGS = {
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
    messages.WARNING: 'alert alert-warning',
    messages.ERROR: 'alert alert-danger',
}