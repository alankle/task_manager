from django.urls import path, register_converter
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from .views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
    create_task_and_add_to_sprint,
    create_task_on_sprint,
    task_by_date,
)
from . import views, converters

register_converter(converters.DateConverter, "yyyymmdd")
handler404 = 'tasks.views.custom_404'

app_name = "tasks"  # This is for namespacing the URLs
urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("help/", TemplateView.as_view(template_name="help.html"), name="help"),
    path("tasks/", TaskListView.as_view(), name="task-list"), #GET
    path("tasks/new/", TaskCreateView.as_view(), name="task-create"), # POST
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"), # GET
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(),name="task-update"), # PUT/PATCH
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),name="task-delete"), # DELETE
    path("tasks/<yyyymmdd:date>/", task_by_date),
    path("tasks/sprint/add_task/<int:pk>/", create_task_on_sprint, name="task-add-to-sprint")
    
]
