# Generated by Django 3.1 on 2020-09-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='url_name',
            field=models.CharField(editable=False, max_length=200),
        ),
    ]