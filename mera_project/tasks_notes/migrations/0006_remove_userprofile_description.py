# Generated by Django 2.2.6 on 2020-03-06 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_notes', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
    ]