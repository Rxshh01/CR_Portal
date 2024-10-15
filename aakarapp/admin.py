from django.contrib import admin

from . models import TaskZero  ,email_auto

# from . models import TaskOne
from import_export.admin import ImportExportModelAdmin
# Register your models here.
 

admin.site.register(email_auto)

@admin.register(TaskZero)
# @admin.register(TaskOne)
class userdetail(ImportExportModelAdmin):
    pass

from .models import taskOne
@admin.register(taskOne)
class task1_import(ImportExportModelAdmin):
    pass

from .models import taskTwo
@admin.register(taskTwo)
class task2_import(ImportExportModelAdmin):
    pass

from .models import taskThree
@admin.register(taskThree)
class task3_import(ImportExportModelAdmin):
    pass


from .models import taskFour
@admin.register(taskFour)
class task4_import(ImportExportModelAdmin):
    pass

from .models import taskFive
@admin.register(taskFive)
class task5_import(ImportExportModelAdmin):
    pass
from .models import taskSix
@admin.register(taskSix)
class task6_import(ImportExportModelAdmin):
    pass


from .models import taskSeven
@admin.register(taskSeven)
class task7_import(ImportExportModelAdmin):
    pass

from .models import taskEight
@admin.register(taskEight)
class task8_import(ImportExportModelAdmin):
    pass

