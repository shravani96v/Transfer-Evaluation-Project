
from django.db import models
from ..models.model_major import Major
from ..models.model_school import School


class DropDown(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
