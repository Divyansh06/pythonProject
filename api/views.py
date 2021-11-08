from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from . import models, serializers

invalid_data = {'Error': 'Invalid Data!'}


@api_view(['GET'])
@permission_classes([AllowAny])
def api_overview(request):
    api_urls = {
        'Task List': '/api/tasks/',
        'Task Details': '/api/tasks/<str:pk>',
        'Task Create': '/api/tasks-create/',
        'Task Update': '/api/tasks-update/<str:pk>',
        'Task Delete': '/api/tasks-delete/<str:pk>',
        'Workspace List': '/api/workspace/',
        'Workspace Details': '/api/workspace/<str:pk>',
        'Workspace Create': '/api/workspace-create/',
        'Workspace Update': '/api/workspace-update/<str:pk>',
        'Workspace Delete': '/api/workspace-delete/<str:pk>',
    }
    return Response(api_urls)


# Task Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(request):
    task = models.Task.objects.all()
    serializer = serializers.TaskSerializer(task, many=True)
    return Response(serializer)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_details(request, pk):
    task = models.Task.objects.get(id=pk)
    serializer = serializers.TaskSerializer(task, many=False)
    return Response(serializer)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    serializer = serializers.TaskSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def task_update(request, pk):
    task = models.Task.objects.get(id=pk)
    serializer = serializers.TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def task_delete(request, pk):
    task = models.Task.objects.get(id=pk)
    task.delete()
    return Response('SUCCESS')


# Workspace Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def workspace_list(request):
    workspace = models.Workspace.objects.all()
    serializer = serializers.WorkspaceSerializer(workspace, many=True)
    return Response(serializer)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def workspace_details(request, pk):
    workspace = models.Workspace.objects.get(id=pk)
    serializer = serializers.WorkspaceSerializer(workspace, many=False)
    return Response(serializer)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def workspace_create(request):
    serializer = serializers.WorkspaceSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def workspace_update(request, pk):
    workspace = models.Workspace.objects.get(id=pk)
    serializer = serializers.WorkspaceSerializer(instance=workspace, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def workspace_delete(request, pk):
    workspace = models.Workspace.objects.get(id=pk)
    workspace.delete()
    return Response('SUCCESS')
