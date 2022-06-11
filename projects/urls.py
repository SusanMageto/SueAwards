
from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('createproject/', postproject, name="postproject"),
    path('projects/<int:id>/', projects_details, name="projects_details"),
    path('project/edit/<int:id>/', edit_project, name="edit_project"),
    path('project/delete/<int:id>/', delete_project, name="delete_project"),
    path('projects/api/v1/projects/', projectList, name='projects'),
]
