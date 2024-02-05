from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project

# Create your views here.
def index(request):
    projects_list = Project.objects.order_by("title")
    context = {"projects_list": projects_list}
    return render(request, "projects/index.html", context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "projects/detail.html", {"project": project})

def title(request, project_id):
    response = 'You are looking at the title of project %s.'
    return HttpResponse(response % project_id)

def project_image_view(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
        
    else:
        form = ProjectForm()
    return render(request, 'projects/img_upload.html', {'form':form})

def success(request):
    return HttpResponse('successfully uploaded')