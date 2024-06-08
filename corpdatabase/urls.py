from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # 管理サイトのパスに名前を付ける
    path('', include('corp.urls')),                # アプリケーションのURLを含める
]
