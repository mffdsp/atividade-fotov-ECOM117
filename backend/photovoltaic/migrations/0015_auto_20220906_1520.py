# Generated by Django 3.2 on 2022-09-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photovoltaic', '0014_settings_days_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvstring',
            name='current_alert',
            field=models.CharField(choices=[('NM', 'Normal'), ('WA', 'Warning'), ('FT', 'Fault'), ('NR', 'Not Rated')], default='NM', max_length=2),
        ),
        migrations.AlterField(
            model_name='pvstring',
            name='voltage_alert',
            field=models.CharField(choices=[('NM', 'Normal'), ('WA', 'Warning'), ('FT', 'Fault'), ('NR', 'Not Rated')], default='NM', max_length=2),
        ),
    ]