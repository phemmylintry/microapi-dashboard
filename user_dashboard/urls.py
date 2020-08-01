from django.urls import path, re_path
from . import views

app_name = "user_dashboard"

urlpatterns = [
    path('', views.api_list, name='dashboard'),
    re_path(r'^adding_api/(?P<id>\d+)$', views.adding_api, name='adding_api'),
    re_path(r'^rmv_api/(?P<id>\d+)$', views.rmv_api, name='rmv_api'),
    path('configure_api/', views.configure_api, name='configure_api'),
    path('logout/', views.logout, name='logout'),
    path('settings/', views.settings, name='settings')
]