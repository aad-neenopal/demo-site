# Generated by Django 5.1.2 on 2024-10-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
