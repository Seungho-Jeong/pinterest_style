# Generated by Django 3.2 on 2021-04-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_auto_20210408_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
    ]