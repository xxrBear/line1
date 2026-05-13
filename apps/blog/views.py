from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.cache import cache_page


class BlogView(View):
    def get(self, request):
        return render(request, 'blog/base.html')


@cache_page(timeout=60)
def now(request):
    now = datetime.now()
    return HttpResponse(str(now))
