from django.views import View
from django.shortcuts import render


class AdminView(View):
    def get(self, request):
        return render(request, 'admin/admin.html')
