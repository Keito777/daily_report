'''
settings.py内の全ての環境変数を読み込み、DEBUG, ALLOWED_HOSTS, DATABASESをオーバーライド
※importしたモジュール（Path, load_dotenvなど）も含まれる
'''
from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']

#開発環境用のDB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}