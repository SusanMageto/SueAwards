from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def home(request):
    projects = Project.objects.all()
    proje = Project.objects.all().order_by('-id')[0]

    context={
        'proje':proje,
        'projects':projects,
    }
    return render(request, 'home.html',context)   



def edit_project(request, id):
    project = get_object_or_404(Project, id = id)
    

    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        messages.success(request,"post was updated successfully")
        return redirect('home')
    context = {
        'project':project,
        'form':form,
    }
    return render(request, 'updateproject.html', context)    
    
def postproject(request):
    if request.user.is_authenticated:
        form = ProjectForm() 
        if request.method == "POST":
            form = ProjectForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                project = form.save(commit=False)   
                project.user = request.user
                project.save()
                messages.success(request,"post was added successfully")
                return redirect('home')
    
        context = {
            'form':form,
        }
        return render(request, 'postprojectpage.html', context)

@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id = id)
    project.delete()
    messages.success(request,"post was deleted successfully")
    return redirect('user_page')



def projects_details(request, id):
    
    project = get_object_or_404(Project, id = id)
    rating = Review.objects.filter(project=project).order_by('-id')


    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
           
            
        if form.is_valid():  
                review = form.save(commit=False)   
                review.user = request.user
                review.project = project
                review.save()
                messages.success(request,"reviews added successfully")
                return redirect('projects_details', id=project.id)
    
    context = {
        'project':project,
        'form':form,
        'rating':rating,
    }
    
    return render(request, 'details.html', context)



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response



@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)  