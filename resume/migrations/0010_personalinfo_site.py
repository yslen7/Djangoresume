# Generated by Django 2.0.2 on 2018-02-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20180224_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='site',
            field=models.URLField(blank=True),
        ),
    ]