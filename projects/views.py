from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404

from .models import Project

# Create your views here.
def index(request):
    latest_project_list = Project.objects.order_by("-pub_date")[:5]
    context = {
        "latest_project_list": latest_project_list
    }
    return render(request, "projects/index.html", context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "projects/detail.html", {"project": project})

def title(request, project_id):
    response = 'You are looking at the title of project %s.'
    return HttpResponse(response % project_id)
