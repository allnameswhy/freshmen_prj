from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(Table)
admin.site.register(Item)
admin.site.register(ColumnText)
admin.site.register(ColumnNumber)
admin.site.register(ColumnName)
admin.site.register(ColumnLocation)
admin.site.register(ColumnImage)
admin.site.register(ColumnFile)

