from django.contrib import admin
import datetime
from . import models
from django.db.models.functions import Upper


def publish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish.short_description = "Publish selected items (will appear on main site)"


def unpublish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish.short_description = "Unpublish selected items (will not appear on main site)"


# Inlines, for m2m relationships in add/update forms in admin dashboard
# There are a lot, as most main models have m2m relationships with other main models both ways


class AuthorLinguisticFieldInline(admin.TabularInline):
    model = models.Author.linguistic_field.through


class AuthorLinguisticNotionInline(admin.TabularInline):
    model = models.Author.linguistic_notion.through


class AuthorLinguisticTraditionInline(admin.TabularInline):
    model = models.Author.linguistic_tradition.through


class AuthorReferenceInline(admin.TabularInline):
    model = models.Author.reference.through


class AuthorSanskritWordInline(admin.TabularInline):
    model = models.Author.sanskrit_word.through


class AuthorTextInline(admin.TabularInline):
    model = models.Author.text.through


class AuthorTextPassageInline(admin.TabularInline):
    model = models.Author.text_passage.through


class LinguisticFieldLinguisticNotionInline(admin.TabularInline):
    model = models.LinguisticField.linguistic_notion.through


class LinguisticFieldLinguisticTraditionInline(admin.TabularInline):
    model = models.LinguisticField.linguistic_tradition.through


class LinguisticFieldReferenceInline(admin.TabularInline):
    model = models.LinguisticField.reference.through


class LinguisticFieldSanskritWordInline(admin.TabularInline):
    model = models.LinguisticField.sanskrit_word.through


class LinguisticFieldTextInline(admin.TabularInline):
    model = models.LinguisticField.text.through


class LinguisticFieldTextPassageInline(admin.TabularInline):
    model = models.LinguisticField.text_passage.through


class LinguisticNotionLinguisticTraditionInline(admin.TabularInline):
    model = models.LinguisticNotion.linguistic_tradition.through


class LinguisticNotionReferenceInline(admin.TabularInline):
    model = models.LinguisticNotion.reference.through


class LinguisticNotionSanskritWordInline(admin.TabularInline):
    model = models.LinguisticNotion.sanskrit_word.through


class LinguisticNotionTextInline(admin.TabularInline):
    model = models.LinguisticNotion.text.through


class LinguisticNotionTextPassageInline(admin.TabularInline):
    model = models.LinguisticNotion.text_passage.through


class LinguisticTraditionReferenceInline(admin.TabularInline):
    model = models.LinguisticTradition.reference.through


class LinguisticTraditionSanskritWordInline(admin.TabularInline):
    model = models.LinguisticTradition.sanskrit_word.through


class LinguisticTraditionTextInline(admin.TabularInline):
    model = models.LinguisticTradition.text.through


class LinguisticTraditionTextPassageInline(admin.TabularInline):
    model = models.LinguisticTradition.text_passage.through


class ReferenceSanskritWordInline(admin.TabularInline):
    model = models.Reference.sanskrit_word.through


class ReferenceTextInline(admin.TabularInline):
    model = models.Reference.text.through


class ReferenceTextPassageInline(admin.TabularInline):
    model = models.Reference.text_passage.through


class SanskritWordTextInline(admin.TabularInline):
    model = models.SanskritWord.text.through


class SanskritWordTextPassageInline(admin.TabularInline):
    model = models.SanskritWord.text_passage.through


# Generic Admin View


class GenericAdminView(admin.ModelAdmin):
    """
    This is a generic class that can be applied to most models to customise their inclusion in the Django admin.

    This class can either be inherited from to customise, e.g.:
    class [ModelName]AdminView(GenericAdminView):

    Or if you don't need to customise it just register a model, e.g.:
    admin.site.register([model name], GenericAdminView)
    """
    list_display = ('id', 'name', 'dynamic_subtitle', 'admin_published', 'meta_created_datetime')
    list_display_links = ('id', 'name')
    list_filter = ('admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    ordering = (Upper('name'), 'id',)
    actions = (publish, unpublish)
    readonly_fields = ('meta_created_by', 'meta_created_datetime', 'meta_lastupdated_by', 'meta_lastupdated_datetime', 'meta_firstpublished_datetime')

    def save_model(self, request, obj, form, change):
        """
        Override default save_model, by adding values to automated fields
        """

        # Meta: created by
        if getattr(obj, 'meta_created_by', None) is None:
            obj.meta_created_by = request.user
        # Meta: last updated by
            obj.meta_lastupdated_by = request.user
        # Meta: first published datetime (only set if the first time being published)
        if getattr(obj, 'admin_published', None) is True and getattr(obj, 'meta_firstpublished_datetime', None) is None:
            obj.meta_firstpublished_datetime = datetime.datetime.now()
        # Save
        obj.save()

# Main models


class AuthorAdminView(GenericAdminView):
    """
    Set the Author section of the Django admin
    """
    list_display = ('id', 'name', 'alternative_name', 'dynamic_subtitle', 'location_most_active',
                    'date_active', 'admin_published', 'meta_created_datetime')
    list_filter = ('admin_published', 'meta_created_by')
    search_fields = ('name', 'alternative_name', 'description', 'location_most_active', 'admin_notes')
    filter_horizontal = ('author', 'meta_citation_additional_authors')
    inlines = [AuthorLinguisticFieldInline,
               AuthorLinguisticNotionInline,
               AuthorLinguisticTraditionInline,
               AuthorReferenceInline,
               AuthorSanskritWordInline,
               AuthorTextInline,
               AuthorTextPassageInline]


class LinguisticFieldAdminView(GenericAdminView):
    """
    Set the Linguistic Field section of the Django admin
    """
    exclude = ('author',)
    filter_horizontal = ('linguistic_field', 'meta_citation_additional_authors')
    inlines = [AuthorLinguisticFieldInline,
               LinguisticFieldLinguisticNotionInline,
               LinguisticFieldLinguisticTraditionInline,
               LinguisticFieldReferenceInline,
               LinguisticFieldSanskritWordInline,
               LinguisticFieldTextInline,
               LinguisticFieldTextPassageInline]


class LinguisticNotionAdminView(GenericAdminView):
    """
    Set the Linguistic Notion section of the Django admin
    """
    exclude = ('author', 'linguistic_field')
    filter_horizontal = ('linguistic_notion', 'meta_citation_additional_authors')
    inlines = [AuthorLinguisticNotionInline,
               LinguisticFieldLinguisticNotionInline,
               LinguisticNotionLinguisticTraditionInline,
               LinguisticNotionReferenceInline,
               LinguisticNotionSanskritWordInline,
               LinguisticNotionTextInline,
               LinguisticNotionTextPassageInline]


class LinguisticTraditionAdminView(GenericAdminView):
    """
    Set the Linguistic Tradition section of the Django admin
    """
    list_display = ('id', 'name', 'dynamic_subtitle', 'linguistic_tradition_group', 'admin_published', 'meta_created_datetime')
    list_filter = ('linguistic_tradition_group', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion')
    filter_horizontal = ('linguistic_tradition', 'meta_citation_additional_authors')
    inlines = [AuthorLinguisticTraditionInline,
               LinguisticFieldLinguisticTraditionInline,
               LinguisticNotionLinguisticTraditionInline,
               LinguisticTraditionReferenceInline,
               LinguisticTraditionSanskritWordInline,
               LinguisticTraditionTextInline,
               LinguisticTraditionTextPassageInline]


class ReferenceAdminView(GenericAdminView):
    """
    Set the Reference section of the Django admin
    """
    list_display = ('id', 'title', 'subtitle', 'authors_list', 'book_title', 'location', 'year', 'reference_type',
                    'reference_publisher', 'admin_published', 'meta_created_datetime')
    list_display_links = ('id', 'title')
    list_filter = ('reference_type', 'reference_publisher', 'admin_published', 'meta_created_by')
    search_fields = ('title', 'subtitle', 'authors_list', 'editors', 'school', 'book_title',
                     'journal_title', 'volume', 'number', 'location', 'year', 'url', 'public_notes', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion', 'linguistic_tradition')
    ordering = (Upper('authors_list'), 'year', Upper('title'), 'id')
    filter_horizontal = ('reference', 'meta_citation_additional_authors')
    inlines = [AuthorReferenceInline,
               LinguisticFieldReferenceInline,
               LinguisticNotionReferenceInline,
               LinguisticTraditionReferenceInline,
               ReferenceSanskritWordInline,
               ReferenceTextInline,
               ReferenceTextPassageInline]


class SanskritWordAdminView(GenericAdminView):
    """
    Set the Sanskrit Word section of the Django admin
    """
    exclude = ('author', 'linguistic_field', 'linguistic_notion', 'linguistic_tradition',
               'reference')
    filter_horizontal = ('sanskrit_word', 'meta_citation_additional_authors')
    inlines = [AuthorSanskritWordInline,
               LinguisticFieldSanskritWordInline,
               LinguisticNotionSanskritWordInline,
               LinguisticTraditionSanskritWordInline,
               ReferenceSanskritWordInline,
               SanskritWordTextInline,
               SanskritWordTextPassageInline]


class TextAdminView(GenericAdminView):
    """
    Set the Text section of the Django admin
    """
    list_display = ('id', 'name', 'alternative_name', 'dynamic_subtitle', 'approximate_date_of_creation', 'location', 'author_main',
                    'text_group', 'text_type', 'admin_published', 'meta_created_datetime')
    list_filter = ('text_group', 'text_type', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'alternative_name', 'description', 'approximate_date_of_creation', 'location', 'author_main', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion', 'linguistic_tradition',
               'reference', 'sanskrit_word')
    filter_horizontal = ('text', 'meta_citation_additional_authors')
    inlines = [AuthorTextInline,
               LinguisticFieldTextInline,
               LinguisticNotionTextInline,
               LinguisticTraditionTextInline,
               ReferenceTextInline,
               SanskritWordTextInline]


class TextPassageAdminView(GenericAdminView):
    """
    Set the Text section of the Django admin
    """
    list_display = ('id', 'name', 'dynamic_subtitle', 'text', 'text_type',
                    'admin_published', 'meta_created_datetime')
    list_filter = ('text_type', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion', 'linguistic_tradition',
               'reference', 'sanskrit_word')
    filter_horizontal = ('text_passage', 'meta_citation_additional_authors')
    inlines = [AuthorTextPassageInline,
               LinguisticFieldTextPassageInline,
               LinguisticNotionTextPassageInline,
               LinguisticTraditionTextPassageInline,
               ReferenceTextPassageInline,
               SanskritWordTextPassageInline]


# Register models and their respective admin view

# Select List models
admin.site.register(models.SlLinguisticTraditionGroup, GenericAdminView)
admin.site.register(models.SlReferencePublisher, GenericAdminView)
admin.site.register(models.SlReferenceType, GenericAdminView)
admin.site.register(models.SlTextGroup, GenericAdminView)
admin.site.register(models.SlTextType, GenericAdminView)

# Main models
admin.site.register(models.Author, AuthorAdminView)
admin.site.register(models.LinguisticField, LinguisticFieldAdminView)
admin.site.register(models.LinguisticNotion, LinguisticNotionAdminView)
admin.site.register(models.LinguisticTradition, LinguisticTraditionAdminView)
admin.site.register(models.Reference, ReferenceAdminView)
admin.site.register(models.SanskritWord, SanskritWordAdminView)
admin.site.register(models.Text, TextAdminView)
admin.site.register(models.TextPassage, TextPassageAdminView)
