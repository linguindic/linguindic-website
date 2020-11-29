# Generated by Django 3.1.3 on 2020-11-29 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('alternative_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location_most_active', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'db_table': 'researchdata_main_author',
            },
        ),
        migrations.CreateModel(
            name='LinguisticField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linguisticfield_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linguisticfield_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_main_linguisticfield',
            },
        ),
        migrations.CreateModel(
            name='LinguisticNotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('example', models.TextField(blank=True, null=True)),
                ('star_count', models.IntegerField(default=0)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('author', models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_linguisticnotion', to='researchdata.Author')),
            ],
            options={
                'db_table': 'researchdata_main_linguisticnotion',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('editors', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.CharField(blank=True, max_length=255, null=True)),
                ('book_title', models.CharField(blank=True, max_length=255, null=True)),
                ('journal_title', models.CharField(blank=True, max_length=255, null=True)),
                ('volume', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('page_start', models.CharField(blank=True, max_length=255, null=True)),
                ('page_end', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('last_accessed_date', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reference_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reference_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_main_reference',
            },
        ),
        migrations.CreateModel(
            name='SlTextGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sltextgroup_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sltextgroup_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_sl_textgroup',
            },
        ),
        migrations.CreateModel(
            name='SlTextType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sltexttype_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sltexttype_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_sl_texttype',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('approximate_date_of_creation', models.CharField(blank=True, max_length=200, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='text_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='text_lastupdated_by', to=settings.AUTH_USER_MODEL)),
                ('reference', models.ManyToManyField(blank=True, db_table='researchdata_m2m_text_reference', to='researchdata.Reference')),
                ('text_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.sltextgroup')),
                ('text_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.sltexttype')),
            ],
            options={
                'db_table': 'researchdata_main_text',
            },
        ),
        migrations.CreateModel(
            name='SlReferenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='slreferencetype_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='slreferencetype_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_sl_referencetype',
            },
        ),
        migrations.CreateModel(
            name='SlReferencePublisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='slreferencepublisher_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='slreferencepublisher_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_sl_referencepublisher',
            },
        ),
        migrations.CreateModel(
            name='SlLinguisticTraditionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sllinguistictraditiongroup_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sllinguistictraditiongroup_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_sl_linguistictraditiongroup',
            },
        ),
        migrations.CreateModel(
            name='SlLinguisticTradition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('linguistic_tradition_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.sllinguistictraditiongroup')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sllinguistictradition_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sllinguistictradition_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_sl_linguistictradition',
            },
        ),
        migrations.CreateModel(
            name='SlLinguisticNotionsRelationshipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('meta_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sllinguisticnotionsrelationshiptype_created_by', to=settings.AUTH_USER_MODEL)),
                ('meta_lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sllinguisticnotionsrelationshiptype_lastupdated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'researchdata_sl_linguisticnotionsrelationshiptype',
            },
        ),
        migrations.AddField(
            model_name='reference',
            name='reference_publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slreferencepublisher'),
        ),
        migrations.AddField(
            model_name='reference',
            name='reference_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slreferencetype'),
        ),
        migrations.CreateModel(
            name='M2MLinguisticNotionsRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linguistic_notion_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linguistic_notion_1', to='researchdata.linguisticnotion')),
                ('linguistic_notion_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linguistic_notion_2', to='researchdata.linguisticnotion')),
                ('linguistic_notions_relationship_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='researchdata.sllinguisticnotionsrelationshiptype')),
            ],
            options={
                'db_table': 'researchdata_m2m_linguisticnotions',
            },
        ),
        migrations.AddField(
            model_name='linguisticnotion',
            name='linguistic_notion',
            field=models.ManyToManyField(related_name='_linguisticnotion_linguistic_notion_+', through='researchdata.M2MLinguisticNotionsRelationship', to='researchdata.LinguisticNotion'),
        ),
        migrations.AddField(
            model_name='linguisticnotion',
            name='linguisticfield',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticfield_linguisticnotion', to='researchdata.LinguisticField'),
        ),
        migrations.AddField(
            model_name='linguisticnotion',
            name='meta_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linguisticnotion_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='linguisticnotion',
            name='meta_lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linguisticnotion_lastupdated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='linguisticnotion',
            name='reference',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticnotion_reference', to='researchdata.Reference'),
        ),
        migrations.AddField(
            model_name='linguisticnotion',
            name='text',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_linguisticnotion_text', to='researchdata.Text'),
        ),
        migrations.AddField(
            model_name='author',
            name='linguistic_tradition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.sllinguistictradition'),
        ),
        migrations.AddField(
            model_name='author',
            name='meta_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='author',
            name='meta_lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author_lastupdated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='author',
            name='reference',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_reference', to='researchdata.Reference'),
        ),
        migrations.AddField(
            model_name='author',
            name='text',
            field=models.ManyToManyField(blank=True, db_table='researchdata_m2m_author_text', to='researchdata.Text'),
        ),
    ]