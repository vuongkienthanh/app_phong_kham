# Generated by Django 3.0.5 on 2020-04-27 07:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('init_quantity', models.PositiveIntegerField(default=0)),
                ('curr_quantity', models.PositiveIntegerField(default=0)),
                ('usage_unit', models.CharField(default='viên', max_length=10)),
                ('sale_unit', models.CharField(default='viên', max_length=10)),
                ('purchase_price', models.PositiveIntegerField()),
                ('sale_price', models.PositiveIntegerField()),
                ('intake_method', models.CharField(default='uống', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=60)),
                ('gender', models.SmallIntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('birthdate', models.DateField()),
                ('address', models.CharField(blank=True, max_length=600)),
                ('past_history', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_datetime', models.DateTimeField(auto_now=True)),
                ('diagnosis', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('days', models.PositiveSmallIntegerField()),
                ('followup_note', models.TextField(blank=True)),
                ('bill', models.PositiveIntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='LineDrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage_once', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.RegexValidator('^\\d+[./]?\\d?$')])),
                ('times_per_day', models.PositiveSmallIntegerField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('usage', models.CharField(max_length=20)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.DrugWarehouse')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Visit')),
            ],
        ),
    ]
