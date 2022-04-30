from django.contrib import admin
from .models import Questionnaire, XWeightage, YWeightage
# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(XWeightage)
admin.site.register(YWeightage)