from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from . import models, serializers
from accounts.serializers import UserSerializer

invalid_data = {'Error': 'Invalid Data!'}


def error_message(key):
    return Response({"Error": f"Missing or Null value field '{key}' in the request body."})


def verify_key(key, request):
    if key not in request.data:
        return False
    elif not request.data.get(key):
        return False
    else:
        return True


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
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_list(request):
    user_id = request.user.id
    if not verify_key('workspace_id', request):
        return error_message('workspace_id')
    workspace_id = request.data.get('workspace_id')
    task = models.Task.objects.filter(user_id=user_id, workspace_id=workspace_id)
    serializer = serializers.TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_details(request, pk):
    user_id = request.user.id
    task = models.Task.objects.filter(id=pk, user_id=user_id)
    serializer = serializers.TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    request.data['user_id'] = request.user.id

    if not verify_key('workspace_id', request):
        return error_message('workspace_id')

    workspace_id = request.data.get('workspace_id')
    workspace = models.Workspace.objects.filter(id=workspace_id)

    if not workspace:
        return Response({'Error': 'Workspace does not exist'})

    serializer = serializers.TaskSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def task_update(request):
    task_id = request.data.task_id
    task = models.Task.objects.filter(id=task_id)
    serializer = serializers.TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def task_delete(request):
    user_id = request.user.id

    if not verify_key('task_id', request):
        return error_message('task_id')

    task_id = request.data.get('task_id')
    task = models.Task.objects.filter(id=task_id, user_id=user_id)
    if not task:
        return Response({"Error": "Task does not exist!"})
    task.delete()
    return Response('SUCCESS')


# Workspace Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def workspace_list(request):
    user_id = request.user.id
    workspace = models.Workspace.objects.filter(user_id=user_id)
    serializer = serializers.WorkspaceSerializer(workspace, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def workspace_details(request):
    user_id = request.user.id

    if not verify_key('workspace_id', request):
        return error_message('workspace_id')

    workspace_id = request.data.get('workspace_id')
    workspace = models.Workspace.objects.filter(id=workspace_id, user_id=user_id)

    if not workspace:
        return Response({"Error": "No workspace available!"})

    serializer = serializers.WorkspaceSerializer(workspace, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def workspace_create(request):
    user_id = request.user.id
    request.data['user_id'] = user_id
    serializer = serializers.WorkspaceSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def workspace_update(request):
    user_id = request.user.id

    if not verify_key('workspace_id', request):
        return error_message('workspace_id')

    workspace_id = request.data.get('workspace_id')
    workspace = models.Workspace.objects.filter(id=workspace_id, user_id=user_id)

    if not workspace:
        return Response({'Error': "Workspace does not exist!"})

    serializer = serializers.WorkspaceSerializer(instance=workspace, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def workspace_delete(request):
    user_id = request.user.id

    if not verify_key('workspace_id', request):
        return error_message('workspace_id')

    workspace_id = request.data.get('workspace_id')
    workspace = models.Workspace.objects.filter(id=workspace_id, user_id=user_id)
    workspace.delete()
    return Response('SUCCESS')
