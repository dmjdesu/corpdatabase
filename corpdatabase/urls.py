from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),  # 管理サイトのパスに名前を付ける
    path("", include("corp.urls")),
    path("api/", include("api.urls")),  # アプリケーションのURLを含める
]

# 開発中に静的ファイルをサーブするための設定
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
