from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


# Create your models here.

class Patient(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 0
        FEMALE = 1

    name = models.CharField(
        max_length=60,
        db_index=True)
    gender = models.IntegerField(choices=Gender.choices)
    birthdate = models.DateField(blank=False)
    address = models.CharField(max_length=600, blank=True)
    past_history = models.TextField(blank=True)


class Visit(models.Model):
    exam_date = models.DateTimeField(auto_now=True)
    diagnosis = models.CharField(max_length=100)
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), ])
    days = models.IntegerField(
        validators=[MinValueValidator(0), ])
    followup_note = models.TextField(blank=True)
    bill = models.IntegerField(
        validators=[MinValueValidator(0), ])
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE)


class DrugWarehouse(models.Model):
    name = models.CharField(
        max_length=20, db_index=True)
    init_quantity = models.IntegerField(
        validators=[MinValueValidator(0), ],
        default=0)
    curr_quantity = models.IntegerField(
        validators=[MinValueValidator(0), ],
        default=0)
    usage_unit = models.CharField(
        max_length=10,
        default='viên')
    sale_unit = models.CharField(
        max_length=10,
        default='viên')
    purchase_price = models.IntegerField(
        validators=[MinValueValidator(0), ])
    sale_price = models.IntegerField(
        validators=[MinValueValidator(0), ])
    intake_method = models.CharField(
        max_length=50,
        default='uống')


class LineDrug(models.Model):
    drug = models.ForeignKey(
        DrugWarehouse,
        on_delete=models.PROTECT)
    dosage_once = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[RegexValidator(r"^\d+[./]?\d?$"), ])
    times_per_day = models.IntegerField(
        validators=[MinValueValidator(0), ])
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), ])
    usage = models.CharField(max_length=20)
    visit = models.ForeignKey(
        Visit,
        on_delete=models.CASCADE)
