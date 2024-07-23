from django.shortcuts import render, redirect
from .forms import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            tel = request.POST.get("tel")
            instance = form.save()
            userbio, created = UserBio.objects.get_or_create(
                tel=tel, for_user_id=instance.id
            )
            if created:
                return JsonResponse(
                    {"message": f"Account creation successful for {email}"}, safe=False
                )
            else:
                return JsonResponse(
                    {"exists": "User with such details already exists"}, safe=False
                )
        else:
            message = form.error_messages
            print(message)
            return JsonResponse({"error": message}, safe=False)
    context = {"form": form}
    return render(request, "auths/signup.html", context)


def sign_in(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("/")
        else:
            return JsonResponse("User doesn't exist.", safe=False)
    return render(request, "auths/signin.html", context={})


def SignOut(request):
    logout(request)
    return redirect("signin")
