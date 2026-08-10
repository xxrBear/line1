from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.urls import path

from apps.users.views import UserRegisterView, healthy

urlpatterns = [
    path('healthy/', healthy, name='healthy'),
    path('register/', UserRegisterView.as_view(), name='register'),
]

if settings.DEBUG is True:
    urlpatterns += debug_toolbar_urls()
