from ninja import NinjaAPI
from tasks.api.tasks import router as tasks_router

api = NinjaAPI()
api.add_router("/tasks/", tasks_router)
