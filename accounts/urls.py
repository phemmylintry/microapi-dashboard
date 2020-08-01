from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('recover/', views.pass_recovery, name='recover'),
    path('logout', views.logout, name="logout"),
    path('recover/sent', views.sent_link, name='sent-link'),
]
