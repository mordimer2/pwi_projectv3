from django.contrib import admin
from .models import Job, Experience, Education, Workflows, Skills 

# Register your models here.
admin.site.register(Job)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Workflows)
admin.site.register(Skills)