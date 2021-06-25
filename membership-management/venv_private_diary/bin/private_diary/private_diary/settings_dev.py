# from .settings_common import *
#
# DEBUG = True
# ALLOWED_HOSTS = []
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#
#     'loggers': {
#
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#         },
#
#         'diary': {
#             'handlers': ['console'],
#             'level': 'DEBUG'
#         },
#     },
#
#
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'Logging.StreamHandler',
#             'formatter': 'dev'
#         },
#     },
#     'formatters': {
#         'dev': {
#             'format': '\t'.join([
#                 '%(asctime)s',
#                 '[%(levelname)s]',
#                 '%(pathname)s(Line:%(lineno)d)',
#                 '%(message)s'
#             ])
#         },
#     }
# }
#
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
