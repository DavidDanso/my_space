# Generated by Django 4.0 on 2022-01-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_projects_project_meeting_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='currency_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
