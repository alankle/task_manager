import datetime
from ninja import ModelSchema, Schema
from pydantic import Field
from .models import Task
from django.contrib.auth.models import User


class TaskSchemaIn(ModelSchema):
    class Config:
        model = Task
        model_fields = ["title", "description"]
        model_fields_optional = ["status"]
        description = "Schema for creating a new task"
    
class TaskSchemaOut(ModelSchema):
    class Config:
        model = Task
        model_fields = ["title", "description"]
        
        
class CreateSchemaOut(Schema):
    id: int
    class Config:
        description = "Schema for the created object output"

class PathDate(Schema):
    year: int = Field(..., ge=1)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    
    def value(self):
        return datetime.date(self.year, self.month, self.day)
