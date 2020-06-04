from django.contrib import admin
from .models.model_school import School
from .models.model_course import Course
from .models.model_approver import Approver
from .models.model_major_requirement import Major_requirement
from .models.model_major import Major
from .models.model_transferevaluation import Transferevaluation

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Approver)
admin.site.register(Major_requirement)
admin.site.register(Major)
admin.site.register(Transferevaluation)
