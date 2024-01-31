from ninja import ModelSchema, Schema
from pydantic import Field
from .models import Task
from django.contrib.auth.models import User


class TaskSchemaIn(ModelSchema):
    class Config:
        model = Task
        model_fields = ["title", "description"]
        model_fields_optional = ["status"]
    
class TaskSchemaOut(ModelSchema):
    
    class Config:
        model = Task
        model_fields = ["title", "description"]
        
class CreateSchemaOut(Schema):
    id: int
