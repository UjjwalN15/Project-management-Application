from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Users
    # tested in Postman
    path('users/register', register, name='register'), # Registers a new user and saved in the database
    path('users/login', Login, name='login'), # Login a new user and gives a new token
    path('users/logout', LogoutView.as_view(), name='logout'), # Logout a user by deleting the token
    path('users/', UserDetailsViewset.as_view({'get': 'list', 'post':'create'}), name='users'), # Get a list of users
    path('users/<int:pk>', UserDetailsViewset.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='user_detail'),
    # Get details of the single user, update and delete a single user
    
    # Projects
    # Tested in postman
    path('projects/', ProjectsViewSet.as_view({'get': 'list', 'post':'create'}), name='projects'),
    # get the list of projects and creates a new post
    path('projects/<int:pk>', ProjectsViewSet.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='projects_detail'),
    # Retrieve, update and delete a post
    
    
    # Tasks
    # Tested in postman
    path('projects/<int:project_pk>/tasks', TaskViewSet.as_view({'get': 'list', 'post':'create'}), name='tasks'),
    # get the list of tasks in a project and creates a new task of a project
    path('tasks/<int:pk>', TaskViewsetDetails.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='tasks_detail'),
    #Retrieve, update and delete a task of a project
    
    
    # Comments
    # Tested in postman
    path('tasks/<int:task_pk>/comments', CommentsViewSet.as_view({'get': 'list', 'post':'create'}), name='comments'),
    # get the list of comments in a task and creates a new comment of a task
    path('comments/<int:pk>', CommentsViewSetDetails.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='comments_detail'),
    # Retrieve, update and delete a comment of a task
]
