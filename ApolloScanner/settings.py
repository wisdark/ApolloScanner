"""
Django settings for ApolloScanner project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!z-9pcl7o65ye9ypha*d&wnzok*8z6b!$q5+d^mce#s++9i_xm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'Assets',
    'Configuration',
    'GithubScan',
    'PathScan',
    'BruteScan',
    'VulnerableScan',
    'VulnerabilityMonitor',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ApolloScanner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ApolloScanner.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Apollo',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SIMPLEUI_CONFIG = {
    # 是否使用系统默认菜单，自定义菜单时建议关闭。
    'system_keep': False,

    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。空列表[] 为全部不显示.
    # 'menu_display': ['资产管理', '扫描任务', '负载管理', '信息收集', '用户管理', '系统配置'],
    'menu_display': ['资产扫描管理', 'Github信息收集', '暴力破解验证', '漏洞扫描验证', '漏洞监控预警', '系统配置管理'],

    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时刷新展示菜单内容。
    # 一般建议关闭。
    'dynamic': True,
    'menus': [
        {
            'app': 'auth',
            'name': '系统配置管理',
            'icon': 'fa fa-cog',
            'models': [
                {
                    'name': '用户管理',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '组管理',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                },
                {
                    'name': '服务配置',
                    'icon': 'fa fa-map',
                    'url': 'Configuration/services/'
                },
                {
                    'name': '服务日志',
                    'icon': 'fa fa-file',
                    'url': 'Configuration/serviceslog/'
                },
                {
                    'name': '系统配置',
                    'icon': 'fa fa-cog',
                    'url': 'Configuration/configuration/'
                }
            ]
        },
        {
            'name': '资产扫描管理',
            'icon': 'fa fa-th-list',
            'models': [
                {
                    'name': '资产任务',
                    'url': 'Assets/assettask',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': '资产列表',
                    'url': 'Assets/assetlist',
                    'icon': 'fa fa-desktop'
                },
            ]
        },
        {
            'name': 'Github信息收集',
            'icon': 'fa fa-search-plus',
            'models': [
                {
                    'name': '收集任务',
                    'url': 'GithubScan/githubscantask',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': '收集结果',
                    'url': 'GithubScan/githubscanresult',
                    'icon': 'fa fa-info'
                },
            ]
        },
        {
            'name': '暴力破解验证',
            'icon': 'fa fa-university',
            'models': [
                {
                    'name': '负载管理',
                    'url': 'BruteScan/bruteregister',
                    'icon': 'fa fa-bolt'
                },
                {
                    'name': '暴破任务',
                    'url': 'BruteScan/brutetasks',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': '暴破结果',
                    'url': 'BruteScan/bruteresult',
                    'icon': 'fa fa-server'
                },
                {
                    'name': '路径暴破',
                    'url': 'PathScan/pathscantask',
                    'icon': 'fa fa-road'
                },
                {
                    'name': '敏感路径',
                    'url': 'PathScan/pathscanresult',
                    'icon': 'fa fa-bars'
                },
            ]
        },
        {
            'name': '漏洞监控预警',
            'icon': 'fa fa-th-list',
            'models': [
                {
                    'name': '监控任务',
                    'url': 'VulnerabilityMonitor/vulnerabilitymonitortask',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': '预警列表',
                    'url': 'VulnerabilityMonitor/vulnerbilitymonitorresult',
                    'icon': 'fa fa-desktop'
                },
            ]
        },
        {
            'name': '漏洞扫描验证',
            'icon': 'fa fa-rocket',
            'models': [
                {
                    'name': '负载管理',
                    'url': 'VulnerableScan/exploitregister',
                    'icon': 'fa fa-bolt'
                },
                {
                    'name': '扫描任务',
                    'url': 'VulnerableScan/vulnerablescantasks',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': '扫描结果',
                    'url': 'VulnerableScan/vulnerablescanresult',
                    'icon': 'fa fa-server'
                },
            ]
        },

    ]
}
CRONJOBS = [
    ('30 9 * * *', 'VulnerabilityMonitor.views.start', ' >> /root/mlog/Monitor.log'), # 注意：/tmp/base_api 目录要手动创建
]