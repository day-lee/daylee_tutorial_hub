from django.contrib import admin
from .models import TutorialList, Tag, Curriculum, Student
# Register your models here.

admin.site.register(TutorialList)
admin.site.register(Tag)
admin.site.register(Student)
admin.site.register(Curriculum)
