# Generated by Django 4.2.5 on 2023-09-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_info_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='day_of_week',
            field=models.CharField(default='Monday', max_length=20),
        ),
    ]
