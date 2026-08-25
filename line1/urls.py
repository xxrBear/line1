from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.urls import path

from apps.user.views import UserLoginView, UserLogoutView, UserRegisterView, healthy

urlpatterns = [
    path('healthy/', healthy, name='healthy'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

if settings.DEBUG is True:
    urlpatterns += debug_toolbar_urls()
