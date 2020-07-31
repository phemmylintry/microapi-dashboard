from django.urls import path
from . import views


urlpatterns = [
    # path('api/', views.api_view)
    path('docs/comment_api', views.commentDocs, name="commentdocs"),
    path('docs/auth_api', views.authDocs, name="authdocs"),
    path('docs/consultant', views.consultant, name="consultant")
]