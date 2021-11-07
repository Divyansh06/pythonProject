from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.api_overview),
    path('create/', views.user_create),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('get-users/', views.user_list),
    path('get-users-django/', views.user_list_django),
    path('get-users/<str:pk>', views.user_details),
]
