from django.contrib import admin
from .models import Patient, Visit, DrugWarehouse, LineDrug, VisitQueue
# Register your models here.

admin.site.register([Patient, Visit, DrugWarehouse, LineDrug, VisitQueue])
