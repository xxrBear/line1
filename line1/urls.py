from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import path

from apps.user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/home/', user_views.user_home, name='user_home'),
]

if settings.DEBUG is True:
    urlpatterns += debug_toolbar_urls()
