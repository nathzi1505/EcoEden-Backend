# Generated by Django 3.0.4 on 2020-07-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_activity_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]