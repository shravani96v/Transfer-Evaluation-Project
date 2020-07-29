from django.db import models
from .model_major import Major

"""
class Major_requirement(models.Model):
    '''
    table name is school
    school_id is the Primarykey
    '''
    major_req_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.description)
"""


class Major_requirement(models.Model):
    """
    table name is Major_requirement
    major_req_id is the Primarykey
    """
    major_req_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, default=None)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('major_id', 'description')

    def __str__(self):
        return str(self.description)

    def major_reqid(self):
        return self.major_req_id
