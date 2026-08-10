from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views import View

from apps.users.forms import UserRegistionForm


def healthy(request):
    return JsonResponse({"message": "ok"}, status=200)


class UserRegisterView(View):
    def post(self, request):
        form = UserRegistionForm(request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)

        form.save()

        return JsonResponse({"message": "User registered successfully."}, status=201)


class UserLoginView(View):
    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)
        return JsonResponse({"message": "User login successfully."})


class UserLogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({"message": "User logged out successfully."})
