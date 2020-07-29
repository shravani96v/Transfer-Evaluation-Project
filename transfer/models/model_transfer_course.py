from django.db import models
from .model_school import School


"""
class TransferCourse(models.Model):

    transfer_course_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True, default=None)
    subject_number = models.CharField(max_length=200,  blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
"""


class TransferCourse(models.Model):
    transfer_course_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True, default=None)
    subject_number = models.CharField(max_length=200,  blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('school_id', 'subject_number')

    def __str__(self):
        return self.title

    def courseid(self):
        return self.transfer_course_id
