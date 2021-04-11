# Generated by Django 3.2 on 2021-04-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0006_auto_20210321_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='linguisticfield',
            name='author',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_linguisticfield', related_name='linguistic_field', to='researchdata.Author'),
        ),
        migrations.AlterField(
            model_name='linguisticfield',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='linguisticnotion',
            name='author',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_linguisticnotion', related_name='linguistic_notion', to='researchdata.Author'),
        ),
        migrations.AlterField(
            model_name='linguisticnotion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='linguisticnotion',
            name='linguistic_field',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticfield_linguisticnotion', related_name='linguistic_notion', to='researchdata.LinguisticField'),
        ),
        migrations.AlterField(
            model_name='linguistictradition',
            name='author',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_linguistictradition', related_name='linguistic_tradition', to='researchdata.Author'),
        ),
        migrations.AlterField(
            model_name='linguistictradition',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='linguistictradition',
            name='linguistic_field',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticfield_linguistictradition', related_name='linguistic_tradition', to='researchdata.LinguisticField'),
        ),
        migrations.AlterField(
            model_name='linguistictradition',
            name='linguistic_notion',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticnotion_linguistictradition', related_name='linguistic_tradition', to='researchdata.LinguisticNotion'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sanskritword',
            name='author',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_sanskritword', related_name='sanskrit_word', to='researchdata.Author'),
        ),
        migrations.AlterField(
            model_name='sanskritword',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sanskritword',
            name='linguistic_field',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticfield_sanskritword', related_name='sanskrit_word', to='researchdata.LinguisticField'),
        ),
        migrations.AlterField(
            model_name='sanskritword',
            name='linguistic_notion',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticnotion_sanskritword', related_name='sanskrit_word', to='researchdata.LinguisticNotion'),
        ),
        migrations.AlterField(
            model_name='sanskritword',
            name='linguistic_tradition',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguistictradition_sanskritword', related_name='sanskrit_word', to='researchdata.LinguisticTradition'),
        ),
        migrations.AlterField(
            model_name='sanskritword',
            name='reference',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_reference_sanskritword', related_name='sanskrit_word', to='researchdata.Reference'),
        ),
        migrations.AlterField(
            model_name='sllinguistictraditiongroup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='slreferencepublisher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='slreferencetype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sltextgroup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sltexttype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='text',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='textpassage',
            name='author',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_textpassage', related_name='text_passage', to='researchdata.Author'),
        ),
        migrations.AlterField(
            model_name='textpassage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='textpassage',
            name='linguistic_field',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticfield_textpassage', related_name='text_passage', to='researchdata.LinguisticField'),
        ),
        migrations.AlterField(
            model_name='textpassage',
            name='linguistic_notion',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticnotion_textpassage', related_name='text_passage', to='researchdata.LinguisticNotion'),
        ),
        migrations.AlterField(
            model_name='textpassage',
            name='linguistic_tradition',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguistictradition_textpassage', related_name='text_passage', to='researchdata.LinguisticTradition'),
        ),
        migrations.AlterField(
            model_name='textpassage',
            name='reference',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_reference_textpassage', related_name='text_passage', to='researchdata.Reference'),
        ),
        migrations.AlterField(
            model_name='textpassage',
            name='sanskrit_word',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_sanskritword_textpassage', related_name='text_passage', to='researchdata.SanskritWord'),
        ),
    ]
