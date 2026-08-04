from django.http import JsonResponse
from django.views import View

from apps.users.forms import UserRegistionForm


class UserRegisterView(View):
    def post(self, request):
        form = UserRegistionForm(request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)

        form.save()

        return JsonResponse({"message": "User registered successfully."}, status=201)
