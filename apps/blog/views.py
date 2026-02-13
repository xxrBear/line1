from django.conf import settings
from django.shortcuts import render
from django.views import View


class BlogView(View):
    def get(self, request):
        print("Django 正在搜寻这些位置:", settings.TEMPLATES[0]['DIRS'])
        return render(request, 'blog/index.html')
