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
    all_apis = ApiList.objects.order_by('title')
    return render(request, 'user_dashboard/dashboard.html', {'all_apis':all_apis})


def adding_api(request, id):
    add_to_api = ApiList.objects.get(id=id)
    user = request.user
    print(user)
    User.add_api(api = add_to_api, name = user)
    #all_apis = ApiList.objects.order_by('title')
    return redirect('/dashboard')
    #return render(request, 'user_dashboard/dashboard.html', {'all_apis':all_apis})

def rmv_api(request, id):
    add_to_api = ApiList.objects.get(id=id)
    user = request.user
    user.api_list.remove(add_to_api)
    return redirect('/dashboard')


@login_required(login_url='/accounts/signin')
def configure_api(request):
    return render(request, 'user_dashboard/configure_api.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def settings(request):
    return render(request, 'user_dashboard/acct_settings.html')


