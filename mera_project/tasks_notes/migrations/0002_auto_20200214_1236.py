# Generated by Django 2.2.6 on 2020-02-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetinfo',
            name='expense',
        ),
        migrations.AddField(
            model_name='budgetinfo',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='budgetinfo',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]