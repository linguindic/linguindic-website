# Generated by Django 3.1.7 on 2021-03-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0004_auto_20210307_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='edition',
        ),
        migrations.AddField(
            model_name='reference',
            name='public_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
