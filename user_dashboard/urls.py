from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ApiView.as_view(), name='dashboard'),
    re_path(r'^addapi/(?P<pk>\d+)$', views.ApiView.as_view(), name='addapi'),
    path('configure_api/', views.ConfigureApiView.as_view(), name='configure_api')
]