from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path

from apps.user import api as user_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/home/', user_api.user_home, name='user_home'),
] + debug_toolbar_urls()
