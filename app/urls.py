from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from app.settings import DEBUG

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
]

if DEBUG:
    urlpatterns +=[
        path("__debug__/", include(debug_toolbar_urls())),
    ]
