# Generated by Django 3.2 on 2022-08-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photovoltaic', '0008_yieldyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvstring',
            name='current_alert',
            field=models.CharField(choices=[('NM', 'Normal'), ('WA', 'Warning'), ('FT', 'Fault')], default='NM', max_length=2),
        ),
        migrations.AddField(
            model_name='pvstring',
            name='voltage_alert',
            field=models.CharField(choices=[('NM', 'Normal'), ('WA', 'Warning'), ('FT', 'Fault')], default='NM', max_length=2),
        ),
    ]