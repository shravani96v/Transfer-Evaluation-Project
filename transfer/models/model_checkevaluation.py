from django.db import models
from .model_major import Major
from .model_school import School

class CheckEvaluation(models.Model):
    """
    Purpose of this table is to have only one record at a time.
    """
    check_eval_id = models.AutoField(primary_key=True)
    approver_choices = (('Yes', 'Yes'), ('No', 'No'))
    major_name = models.CharField(max_length=30)
    school_name = models.CharField(max_length=30)
    #major_name = models.CharField(max_length=40)
    transfer_subject_number = models.CharField(max_length=30)
    transfer_course_title = models.CharField(max_length=30)
    unhm_equivalent = models.CharField(max_length=20)
    approver_name = models.CharField(max_length=20, blank=True, null=True)
    approved_status = models.CharField(max_length=5, choices=approver_choices, default=None)
    sem_or_year_taken = models.CharField(max_length=20, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.check_eval_id)
