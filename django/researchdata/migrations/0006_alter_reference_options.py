# Generated by Django 3.2.7 on 2021-09-18 08:30

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0005_auto_20210709_1202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reference',
            options={'ordering': [django.db.models.functions.text.Upper('authors_list'), 'year', django.db.models.functions.text.Upper('title'), django.db.models.functions.text.Upper('reference_type__name'), 'id']},
        ),
    ]
