# Generated by Django 2.2.7 on 2019-12-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0004_allcourses_startedfrom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(verbose_name='Started from'),
        ),
    ]