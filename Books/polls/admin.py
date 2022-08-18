from django.contrib import admin
from .models import Information, Option, Poll, Choice, Question, Quiz
from auditlog.registry import auditlog

# Register your models here.

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Information)
admin.site.register(Quiz)
admin.site.register(Option)
admin.site.register(Question)

auditlog.register(Information)
auditlog.register(Option)
auditlog.register(Poll)
auditlog.register(Choice)
auditlog.register(Quiz)
auditlog.register(Question)
