from django.db import models


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    major_name = models.CharField(max_length=200, blank=True, null=True)
