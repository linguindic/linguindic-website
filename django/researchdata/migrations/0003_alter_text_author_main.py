# Generated by Django 3.2.4 on 2021-06-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0002_auto_20210616_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='author_main',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Author'),
        ),
    ]
