from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.conf import settings
import requests
import json
from .models import User


HEADERS = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmMjMzNzE2NGM1NjRkMDAwNDBlZDllNyIsImVtYWlsIjoiaWNlYmVla2F5eUBnbWFpbC5jb20iLCJEQlVSSSI6Im1vbmdvZGIrc3J2Oi8vZnVsbHN0YWNrOmZ1bGxzdGFja0BzYW5kYm94LTFsbTRoLm1vbmdvZGIubmV0L2F1dGgtYXBwP3JldHJ5V3JpdGVzPXRydWUiLCJpYXQiOjE1OTYxNDM0NDd9.E_zJqUcM8s0RHKamaE-gQss9Y1F1Nn0TRSu3q_45E58"
        }
BASE_URL = "https://auth-microapi.herokuapp.com"

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard:dashboard")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect("accounts:signin")
    return render(request, "accounts/sign_in.html")


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        confirm_pass = request.POST.get('confirmpwd')
        password = request.POST.get('pwd')
        if password == confirm_pass:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Username Taken, Please try again')
                return redirect('signup')
                

            else:
                url = 'https://auth-microapi.herokuapp.com/api/user/register'
                #url = endpoint.format(api_url=settings.AUTH_API_URL)
                payload = {
                    "username": username,
                    "email": email,
                    "password": password,
                    "phone_number": phonenumber,
                }
                headers = {
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmMjMzNzE2NGM1NjRkMDAwNDBlZDllNyIsImVtYWlsIjoiaWNlYmVla2F5eUBnbWFpbC5jb20iLCJEQlVSSSI6Im1vbmdvZGIrc3J2Oi8vZnVsbHN0YWNrOmZ1bGxzdGFja0BzYW5kYm94LTFsbTRoLm1vbmdvZGIubmV0L2F1dGgtYXBwP3JldHJ5V3JpdGVzPXRydWUiLCJpYXQiOjE1OTYxNDM0NDd9.E_zJqUcM8s0RHKamaE-gQss9Y1F1Nn0TRSu3q_45E58"
                }
                # response = requests.request("POST", url, headers=headers, data = payload)
                response = requests.request(
                    "POST", url, headers=headers, data=payload)

                response = response.json()
                if response['success'] == True:

                    user = User(username=response['data']['username'])
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = response['data']['email']
                    user.user_id = response['data']['id']
                    user.is_active = False
                    user.save()
                    msg = response['message']
                    messages.info(request, f'{msg}')
                    return redirect("accounts:signin")
                else:
                    msg = response['message']
                    messages.info(request, f'{msg}')
                    return redirect("accounts:signup")
        else:
            messages.error(request, 'Password mismatch')
            return redirect("accounts:signup")
    return render(request, "accounts/sign_up.html")


def pass_recovery(request):
    if request.method == "POST":
        email = request.POST.get("email")
        url = BASE_URL + "/api/user/password/reset"
        payload = {
                    "email": email
                }
        response = requests.post(url, headers=HEADERS, data=payload)
        response = response.content.decode("utf8")
        response = json.loads(response)
        print(response)
        if response["success"] == True:
            return redirect("accounts:sent-link")
        else:
            messages.error(request, response["message"])
            print(messages.info)
            return redirect("accounts:recover")
    return render(request, "accounts/recover_password.html")
        

def sent_link(request):
    return render(request, "accounts/reset_link_sent.html")


def logout(request):
    url =  BASE_URL + "/api/user/logout"
    response = requests.get(url, headers=HEADERS)
    print(response.content)
    response = response.content.decode("utf8")
    response = json.loads(response)
    if response["success"] == True:
        auth.logout(request)        
        return redirect("accounts:signin")
    else:
        messages.error(request, "Something went wrong, try again")
        return redirect("dashboard:dashboard")
