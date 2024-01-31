from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Task
from .mixins import SprintTaskMixin
from django.http import HttpRequest, HttpResponseRedirect,Http404, JsonResponse, HttpResponse
from rest_framework import status
from django.shortcuts import render, redirect
from .service import create_task_and_add_to_sprint, claim_task, TaskAlreadyClaimedException
from django.shortcuts import render


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def claim_task_view(request, task_id):
    user_id = request.user.id # Assuming you have access to the  user ID from the request
    try:
        claim_task(user_id, task_id)
        return JsonResponse({'message': 'Task successfully claimed.'})
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist.", status=status.HTTP_404_NOT_FOUND)
    except TaskAlreadyClaimedException:
        return HttpResponse("Task is already claimed or completed.", status=status.HTTP_400_BAD_REQUEST)

def task_by_date(request: HttpRequest):
    pass

def create_task_on_sprint(request: HttpRequest, sprint_id: int) -> HttpResponseRedirect:
    if request.method == 'POST':
        task_data: dict[str, str] = {
        'title': request.POST['title'],
        'description': request.POST.get('description', ""),
        'status': request.POST.get('status', "UNASSIGNED"),
        }
        task = create_task_and_add_to_sprint(task_data, sprint_id, request.user)
        return redirect('task-detail', task_id=task.id)
    raise Http404("Not found")


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
