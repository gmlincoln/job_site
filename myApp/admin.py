from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Custom_User)
admin.site.register(JobSeekerModel)
admin.site.register(RecruiterModel)
admin.site.register(JobModel)
admin.site.register(jobApplyModel)
