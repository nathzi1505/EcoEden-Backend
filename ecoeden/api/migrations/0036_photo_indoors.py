# Generated by Django 3.0.4 on 2020-08-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20200729_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='indoors',
            field=models.BooleanField(default=True),
        ),
    ]