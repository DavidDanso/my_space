# Generated by Django 4.0 on 2022-02-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_user_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]