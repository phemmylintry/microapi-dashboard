from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from . models import ApiList, ActiveApiList
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from homepage.views import index

@login_required(login_url='/accounts/signin')
def api_list(request):
    user = User.objects.all()
    all_apis = ApiList.objects.order_by('title')[:4]
    return render(request, 'user_dashboard/dashboard.html', {'all_apis':all_apis})


def adding_api(request, id):
    add_to_api = ApiList.objects.get(id=id)
    user = User.objects.get(username='FemiSocrates')
    print(user)
    print(User.objects.all().first())
    User.add_api(api = add_to_api, name = user)
    all_apis = ApiList.objects.order_by('title')[:4]
    # return redirect('dashboard')
    return render(request, 'user_dashboard/dashboard.html', {'all_apis':all_apis})


@login_required(login_url='/accounts/signin')
def configure_api(request):
    return render(request, 'user_dashboard/configure_api.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def settings(request):
    return render(request, 'user_dashboard/acct_settings.html')


