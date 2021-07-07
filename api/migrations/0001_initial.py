# Generated by Django 3.2.5 on 2021-07-07 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VaccineSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_slot_code', models.CharField(max_length=20)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hospitals')),
            ],
        ),
        migrations.CreateModel(
            name='OxygenCylinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oxygen_cylinder_code', models.CharField(max_length=20)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hospitals')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hospitals')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Beds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_code', models.CharField(max_length=20)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hospitals')),
            ],
        ),
    ]