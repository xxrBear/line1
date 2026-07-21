from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings

urlpatterns = []

if settings.DEBUG is True:
    urlpatterns += debug_toolbar_urls()
