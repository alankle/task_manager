from http import HTTPStatus
from django.http import Http404, HttpRequest, HttpResponse
from ninja import Router, Path
from ninja.pagination import paginate 
from tasks.schemas import CreateSchemaOut, TaskSchemaIn, TaskSchemaOut, PathDate
from tasks import service
from tasks.enums import TaskStatus

router = Router(tags=["tasks"])

@router.get("/archive/{year}/{month}/{day}", response=list[TaskSchemaOut])
@paginate
def archived_tasks(request, created_at: PathDate = Path(...)):
    return service.search_tasks(created_at=created_at.value(), status=TaskStatus.ARCHIVED.value)


@router.post("/", response={201: CreateSchemaOut})
def create_task(request: HttpRequest, task_in: TaskSchemaIn):
    creator = request.user
    return service.create_task(creator, **task_in.dict())

@router.get("/", response=list[TaskSchemaOut])
@paginate
def list_tasks(request):
    return service.list_tasks()

@router.get("/{int:task_id}", response=TaskSchemaOut)
def get_task(request: HttpRequest, task_id: int):
    task = service.get_task(task_id)
    if task is None:
        raise Http404("Task not found.")
    return task

@router.put("/{int:task_id}")
def update_task(request: HttpRequest, task_id: int, task_data: TaskSchemaIn):
    service.update_task(task_id=task_id, **task_data.dict())
    return HttpResponse(status=HTTPStatus.NO_CONTENT)

@router.delete("/{int:task_id}")
def delete_task(request: HttpRequest, task_id: int):
    service.delete_task(task_id=task_id)
    return HttpResponse(status=HTTPStatus.NO_CONTENT)
