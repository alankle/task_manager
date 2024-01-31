from django.http import HttpRequest
from ninja import Router 
from tasks.schemas import CreateSchemaOut, TaskSchemaIn, TaskSchemaOut

router = Router()

@router.get("/", response=list[TaskSchemaOut])
def list_tasks(request: HttpRequest):
    return [TaskSchemaOut(title="Mock Task", description="Task description")]

@router.post("/", response=CreateSchemaOut)
def create_task(request: HttpRequest, task_in: TaskSchemaIn ):
    return CreateSchemaOut(id=1)

