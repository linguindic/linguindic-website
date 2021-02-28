from django.contrib import admin
from . import models

admin.site.site_header = 'LINGUINDIC: Admin Dashboard'


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
    model = models.Author.linguisticfield.through


class AuthorLinguisticNotionInline(admin.TabularInline):
    model = models.Author.linguisticnotion.through


class AuthorLinguisticTraditionInline(admin.TabularInline):
    model = models.Author.linguistictradition.through


class AuthorReferenceInline(admin.TabularInline):
    model = models.Author.reference.through


class AuthorSanskritWordInline(admin.TabularInline):
    model = models.Author.sanskritword.through


class AuthorTextInline(admin.TabularInline):
    model = models.Author.text.through


class AuthorTextPassageInline(admin.TabularInline):
    model = models.Author.textpassage.through


class LinguisticFieldLinguisticNotionInline(admin.TabularInline):
    model = models.LinguisticField.linguisticnotion.through


class LinguisticFieldLinguisticTraditionInline(admin.TabularInline):
    model = models.LinguisticField.linguistictradition.through


class LinguisticFieldReferenceInline(admin.TabularInline):
    model = models.LinguisticField.reference.through


class LinguisticFieldSanskritWordInline(admin.TabularInline):
    model = models.LinguisticField.sanskritword.through


class LinguisticFieldTextInline(admin.TabularInline):
    model = models.LinguisticField.text.through


class LinguisticFieldTextPassageInline(admin.TabularInline):
    model = models.LinguisticField.textpassage.through


class LinguisticNotionLinguisticTraditionInline(admin.TabularInline):
    model = models.LinguisticNotion.linguistictradition.through


class LinguisticNotionReferenceInline(admin.TabularInline):
    model = models.LinguisticNotion.reference.through


class LinguisticNotionSanskritWordInline(admin.TabularInline):
    model = models.LinguisticNotion.sanskritword.through


class LinguisticNotionTextInline(admin.TabularInline):
    model = models.LinguisticNotion.text.through


class LinguisticNotionTextPassageInline(admin.TabularInline):
    model = models.LinguisticNotion.textpassage.through


class LinguisticTraditionReferenceInline(admin.TabularInline):
    model = models.LinguisticTradition.reference.through


class LinguisticTraditionSanskritWordInline(admin.TabularInline):
    model = models.LinguisticTradition.sanskritword.through


class LinguisticTraditionTextInline(admin.TabularInline):
    model = models.LinguisticTradition.text.through


class LinguisticTraditionTextPassageInline(admin.TabularInline):
    model = models.LinguisticTradition.textpassage.through


class ReferenceSanskritWordInline(admin.TabularInline):
    model = models.Reference.sanskritword.through


class ReferenceTextInline(admin.TabularInline):
    model = models.Reference.text.through


class ReferenceTextPassageInline(admin.TabularInline):
    model = models.Reference.textpassage.through


class SanskritWordTextInline(admin.TabularInline):
    model = models.SanskritWord.text.through


class SanskritWordTextPassageInline(admin.TabularInline):
    model = models.SanskritWord.textpassage.through


# Generic Admin View


class GenericAdminView(admin.ModelAdmin):
    """
    This is a generic class that can be applied to most models to customise their inclusion in the Django admin.

    This class can either be inherited from to customise, e.g.:
    class [ModelName]AdminView(GenericAdminView):

    Or if you don't need to customise it just register a model, e.g.:
    admin.site.register([model name], GenericAdminView)
    """
    list_display = ('id', 'name', 'description', 'admin_published', 'meta_created_datetime')
    list_filter = ('admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    ordering = ('-id',)
    actions = (publish, unpublish)


# Main models


class AuthorAdminView(GenericAdminView):
    """
    Set the Author section of the Django admin
    """
    list_display = ('id', 'first_name', 'last_name', 'alternative_name', 'description', 'location_most_active',
                    'date_of_birth', 'date_of_death', 'admin_published', 'meta_created_datetime')
    list_filter = ('admin_published', 'meta_created_by')
    search_fields = ('first_name', 'last_name', 'alternative_name', 'description', 'location_most_active', 'admin_notes')
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
    list_display = ('id', 'name', 'description', 'linguistic_tradition_group', 'admin_published', 'meta_created_datetime')
    list_filter = ('linguistic_tradition_group', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion')
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
    list_display = ('id', 'title', 'subtitle', 'book_title', 'location', 'year', 'reference_type',
                    'reference_publisher', 'admin_published', 'meta_created_datetime')
    list_filter = ('reference_type', 'reference_publisher', 'admin_published', 'meta_created_by')
    search_fields = ('title', 'subtitle', 'editors', 'school', 'edition', 'book_title',
                     'journal_title', 'volume', 'number', 'location', 'year', 'url', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion', 'linguistic_tradition')
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
    list_display = ('id', 'name', 'description', 'approximate_date_of_creation', 'text_group', 'text_type',
                    'admin_published', 'meta_created_datetime')
    list_filter = ('text_group', 'text_type', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion', 'linguistic_tradition',
               'reference', 'sanskrit_word')
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
    list_display = ('id', 'name', 'description', 'text', 'text_type',
                    'admin_published', 'meta_created_datetime')
    list_filter = ('text_type', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    exclude = ('author', 'linguistic_field', 'linguistic_notion', 'linguistic_tradition',
               'reference', 'sanskrit_word', 'text')
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
