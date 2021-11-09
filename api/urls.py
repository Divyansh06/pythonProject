from django.urls import path
from api import views

urlpatterns = [
    path('', views.api_overview),
    path('tasks/', views.task_list),
    path('tasks/<str:pk>', views.task_details),
    path('tasks-create/', views.task_create),
    path('tasks-update/', views.task_update),
    path('tasks-delete/', views.task_delete),
    path('workspace/', views.workspace_list),
    path('workspace/<str:pk>', views.workspace_details),
    path('workspace-create/', views.workspace_create),
    path('workspace-update/', views.workspace_update),
    path('workspace-delete/', views.workspace_delete),
]
