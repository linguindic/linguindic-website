# Generated by Django 3.1.7 on 2021-03-07 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0005_auto_20210307_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reference',
            old_name='authors',
            new_name='authors_list',
        ),
    ]
