from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Users
    path('users/register', register, name='register'),
    path('users/login', Login, name='login'),
    path('users/logout', LogoutView.as_view(), name='logout'),
    path('users/', UserDetailsViewset.as_view({'get': 'list', 'post':'create'}), name='users'),
    path('users/<int:pk>', UserDetailsViewset.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='user_detail'),
    path('users/logout', LogoutView.as_view(), name='logout'),
    
    # Projects
    path('projects/', ProjectsViewSet.as_view({'get': 'list', 'post':'create'}), name='projects'),
    path('projects/<int:pk>', ProjectsViewSet.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='projects_detail'),
    
    # Tasks
    path('projects/<int:project_pk>/tasks', TaskViewSet.as_view({'get': 'list', 'post':'create'}), name='tasks'),
    path('tasks/<int:pk>', TaskViewsetDetails.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='tasks_detail'),

    # Comments
    path('tasks/<int:task_pk>/comments', CommentsViewSet.as_view({'get': 'list', 'post':'create'}), name='comments'),
    path('comments/<int:pk>', CommentsViewSetDetails.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='comments_detail'),
]
