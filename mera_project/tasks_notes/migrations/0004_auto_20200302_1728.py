# Generated by Django 2.2.6 on 2020-03-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_notes', '0003_auto_20200301_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetinfo',
            name='date_added',
            field=models.DateField(),
        ),
    ]
