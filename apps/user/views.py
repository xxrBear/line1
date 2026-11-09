from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from apps.user.forms import UserRegisterForm


def healthy(request):
    return JsonResponse({"message": "ok"}, status=200)


def home(request):
    return render(request, "base/base.html")


class UserRegisterView(View):
    def get(self, request):
        return render(request, "user/register.html")

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)

        form.save()

        return redirect("login")


class UserLoginView(View):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)
        auth_login(request, form.get_user())
        return redirect("home")


class UserLogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({"message": "User logged out successfully."})


class UserInfoView(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse(
                {"logged_in": False, "message": "Not authenticated."},
                status=401,
            )

        return JsonResponse(
            {
                "logged_in": True,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "date_joined": user.date_joined,
                    "last_login": user.last_login,
                },
            }
        )
