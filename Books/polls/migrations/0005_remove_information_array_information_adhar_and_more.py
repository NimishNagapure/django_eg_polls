# Generated by Django 4.0 on 2022-02-16 08:47

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_information_adhar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='array',
        ),
        migrations.AddField(
            model_name='information',
            name='adhar',
            field=models.ImageField(null=True, upload_to=polls.models.user_profile_picture),
        ),
        migrations.AddField(
            model_name='information',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
