# Generated by Django 5.1.1 on 2024-10-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='blurb',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
