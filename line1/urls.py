from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.urls import path

from apps.user.views import (
    UserInfoView,
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
    healthy,
    home,
)

urlpatterns = [
    path('healthy/', healthy, name='healthy'),
    path('', home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user-info/', UserInfoView.as_view(), name='user-info'),
]

if settings.DEBUG is True:
    urlpatterns += debug_toolbar_urls()
