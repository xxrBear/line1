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
