from django.db import models
from .model_school import School


class Course(models.Model):

    course_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True, default=None)
    subject_number = models.CharField(max_length=200,  blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
