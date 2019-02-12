from django.contrib import admin
from .models import teacher, faculty, course

admin.site.register(teacher)
admin.site.register(course)
admin.site.register(faculty)


# Register your models here.
