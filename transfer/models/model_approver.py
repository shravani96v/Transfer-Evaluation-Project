from django.db import models

"""
class Approver(models.Model):
    approver_id = models.AutoField(primary_key=True)
    approver_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.approver_name
"""


class Approver(models.Model):
    approver_id = models.AutoField(primary_key=True)
    approver_name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.approver_name

    def approverid(self):
        return self.approver_id
