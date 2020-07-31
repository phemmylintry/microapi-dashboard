from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


# # Home page view
# class HomeView(TemplateView):
#     template_name = "homepage/index.html"

# # Home page view
def index(request):
    return render(request, 'homepage/index.html')


# About us view
def about(request):
    return render(request, 'homepage/about.html')


# Contact us page
def contact_us(request):
    context = {}
    return render(request, 'homepage/contact.html', context)


# Views to FAQ
def faq(request):
    return render(request, 'homepage/faq.html')

#View to sign in
def signin(request):
    return render(request, 'accounts/sign_in.html')

#views to sign up
def signup(request):
    return render(request, 'accounts/sign_up.html')
