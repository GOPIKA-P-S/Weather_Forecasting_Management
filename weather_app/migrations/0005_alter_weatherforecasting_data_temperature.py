# Generated by Django 5.0.4 on 2024-05-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0004_alter_weatherforecasting_data_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherforecasting_data',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
