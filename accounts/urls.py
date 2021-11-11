from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.api_overview),
    path('create/', views.user_create),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('user-details/', views.user_details),

    # For testing Purpose only
    path('user-list/', views.user_list),
]
