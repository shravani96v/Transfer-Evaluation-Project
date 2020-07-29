from django.contrib import admin
from .models.model_school import School
from .models.model_transfer_course import TransferCourse
from .models.model_approver import Approver
from .models.model_major_requirement import Major_requirement
from .models.model_major import Major
from .models.model_transferevaluation import Transferevaluation
from .models.model_checkevaluation import CheckEvaluation

admin.site.register(School)
admin.site.register(TransferCourse)
admin.site.register(Approver)
admin.site.register(Major_requirement)
admin.site.register(Major)
admin.site.register(Transferevaluation)
admin.site.register(CheckEvaluation)
