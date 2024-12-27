from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        # Save the user using the serializer's save method, which will handle password hashing
        serializer.save()
        return Response({'message': 'Registration Successful.'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def Login(request):
    # Validate input
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate user
    user = authenticate(username=email, password=password)
    if user is None:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # Generate or retrieve token
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def post(self, request, format=None):
        # Delete the token to force a logout
        request.user.auth_token.delete()
        return Response({"detail": "Logout Successful"}, status=status.HTTP_200_OK)
    

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class TaskViewSet(viewsets.ViewSet):
    
    def list(self, request, project_pk=None):
        # Get all tasks for a specific project
        project = get_object_or_404(Projects, pk=project_pk)
        tasks = Tasks.objects.filter(project=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    
    def create(self, request, project_pk=None):
        # Retrieve the project from the URL (the project_pk automatically comes from the URL)
        project = get_object_or_404(Projects, pk=project_pk)
        
        # Create the task using the provided data and associate it with the retrieved project
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the task and associate it with the retrieved project
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskViewsetDetails(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskDetailSerializer
    


class CommentsViewSet(viewsets.ViewSet):
    
    def list(self, request, task_pk=None):
        task = get_object_or_404(Tasks, pk=task_pk)
        comments = Comments.objects.filter(task=task)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, task_pk=None):
        task = get_object_or_404(Tasks, pk=task_pk)
        data = request.data
        data['task'] = task.id
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsViewSetDetails(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsDetailSerializer