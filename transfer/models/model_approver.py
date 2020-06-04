from django.db import models


class Approver(models.Model):
    approver_id = models.AutoField(primary_key=True)
    approver_name = models.CharField(max_length=200, blank=True, null=True)


def __str__(self):
    return self.text[:50]
