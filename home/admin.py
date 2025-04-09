from django.contrib import admin
from .models import Profile, Mail, SaveDatasM, CompanyCodeModel

# Register your models here.
admin.site.register(Profile)
admin.site.register(Mail)
admin.site.register(SaveDatasM)
admin.site.register(CompanyCodeModel)