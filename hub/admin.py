from django.contrib import admin
from .models import *
from .models import TutorialList, Tag, Curriculum, Student, Customer, CurriculumItem
# Register your models here.

admin.site.register(TutorialList)
admin.site.register(Tag)
admin.site.register(Student)
admin.site.register(Curriculum)
admin.site.register(Customer)
admin.site.register(CurriculumItem)

