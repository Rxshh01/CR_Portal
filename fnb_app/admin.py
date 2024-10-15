from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import fnb_model 
@admin.register(fnb_model)
class task4_import(ImportExportModelAdmin):
    pass
from .models import pitch_submission
@admin.register(pitch_submission)
class pitch(ImportExportModelAdmin):
    pass
