from django.db import models
from .model_major import Major


class Major_requirement(models.Model):
    """
    table name is school
    school_id is the Primarykey
    """
    major_req_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)
