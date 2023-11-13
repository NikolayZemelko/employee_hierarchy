# Generated by Django 4.2.7 on 2023-11-13 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_offered',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='employees.employee'),
        ),
    ]
