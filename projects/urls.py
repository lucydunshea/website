from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import project_image_view, success
from . import views

app_name="projects"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:project_id>/", views.detail, name="title"),
    path('image_upload', project_image_view, name='image_upload'),
    path('success', success, name='success')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)