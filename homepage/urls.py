from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('contact_us/', views.contact_us, name="contact"),
    path('faq/', views.faq, name="faq"),
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('recover_password/',views.recover_password, name="recover_password"),
    path('reset_link/',views.reset_link, name="reset_link"),
    path('reset_password/',views.reset_password, name="reset_password")
]