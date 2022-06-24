# Generated by Django 4.0.5 on 2022-06-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentClass',
            fields=[
                ('equipment_class', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('billing_code', models.CharField(max_length=20)),
                ('rates', models.PositiveIntegerField(blank=True)),
                ('active', models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1)),
            ],
            options={
                'db_table': 'EquipmentCode',
            },
        ),
        migrations.CreateModel(
            name='LaborClass',
            fields=[
                ('labor_class', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('billing_code', models.CharField(max_length=20)),
                ('rates', models.PositiveIntegerField(blank=True)),
                ('active', models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1)),
            ],
            options={
                'db_table': 'LaborCode',
            },
        ),
        migrations.CreateModel(
            name='SupplyClass',
            fields=[
                ('supply_class', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('billing_code', models.CharField(max_length=20)),
                ('rates', models.PositiveIntegerField(blank=True)),
                ('active', models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1)),
            ],
            options={
                'db_table': 'SupplyCode',
            },
        ),
    ]
