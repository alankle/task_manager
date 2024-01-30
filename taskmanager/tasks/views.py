from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Task
from .mixins import SprintTaskMixin

class TaskListView(ListView):
    model = Task
    template_name = "/tasks/task_list.html"
    context_object_name = "tasks"
    
class TaskDetailView(DetailView):
    model = Task
    template_name = "/tasks/task_detail.html"
    context_object_name = "task"
    
class TaskCreateView(SprintTaskMixin, CreateView):
    model = Task
    template_name = "/tasks/task_form.html"
    fields = ("name", "description", "start_date", "end_date")
    
    def get_success_url(self):
        return reverse_lazy("task-detail", kwargs={"pk":self.object.id})

class TaskUpdateView(SprintTaskMixin, UpdateView):
    model = Task
    template_name = "/tasks/task_form.html"
    fields = ("name", "description", "start_date", "end_date")
    
    def get_success_url(self):
        return reverse_lazy("task-detail", kwargs={"pk": self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "/tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")
