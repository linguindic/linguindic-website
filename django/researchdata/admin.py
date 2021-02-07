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


# Select List models


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
    ordering = ('-id',)
    actions = (publish, unpublish)


class LinguisticTraditionAdminView(GenericAdminView):
    """
    Set the Linguistic Tradition section of the Django admin
    """
    list_display = ('id', 'name', 'description', 'linguistic_tradition_group', 'admin_published', 'meta_created_datetime')
    list_filter = ('linguistic_tradition_group', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    ordering = ('-id',)
    actions = (publish, unpublish)


class ReferenceAdminView(GenericAdminView):
    """
    Set the Reference section of the Django admin
    """
    list_display = ('id', 'title', 'subtitle', 'book_title', 'location', 'year', 'reference_type',
                    'reference_publisher', 'admin_published', 'meta_created_datetime')
    list_filter = ('reference_type', 'reference_publisher', 'admin_published', 'meta_created_by')
    search_fields = ('title', 'subtitle', 'editors', 'school', 'edition', 'book_title',
                     'journal_title', 'volume', 'number', 'location', 'year', 'url', 'admin_notes')
    ordering = ('-id',)
    actions = (publish, unpublish)


class TextAdminView(GenericAdminView):
    """
    Set the Text section of the Django admin
    """
    list_display = ('id', 'name', 'description', 'approximate_date_of_creation', 'text_group', 'text_type',
                    'admin_published', 'meta_created_datetime')
    list_filter = ('text_group', 'text_type', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    ordering = ('-id',)
    actions = (publish, unpublish)


class TextPassageAdminView(GenericAdminView):
    """
    Set the Text section of the Django admin
    """
    list_display = ('id', 'name', 'description', 'text', 'text_type',
                    'admin_published', 'meta_created_datetime')
    list_filter = ('text_type', 'admin_published', 'meta_created_by')
    search_fields = ('name', 'description', 'admin_notes')
    ordering = ('-id',)
    actions = (publish, unpublish)


# Register models and their respective admin view

# Select List models
admin.site.register(models.SlLinguisticTraditionGroup, GenericAdminView)
admin.site.register(models.SlReferencePublisher, GenericAdminView)
admin.site.register(models.SlReferenceType, GenericAdminView)
admin.site.register(models.SlTextGroup, GenericAdminView)
admin.site.register(models.SlTextType, GenericAdminView)

# Main models
admin.site.register(models.Author, AuthorAdminView)
admin.site.register(models.LinguisticField, GenericAdminView)  # Note - uses GenericAdminView
admin.site.register(models.LinguisticNotion, GenericAdminView)  # Note - uses GenericAdminView
admin.site.register(models.LinguisticTradition, LinguisticTraditionAdminView)
admin.site.register(models.Reference, ReferenceAdminView)
admin.site.register(models.SanskritWord, GenericAdminView)  # Note - uses GenericAdminView
admin.site.register(models.Text, TextAdminView)
admin.site.register(models.TextPassage, TextPassageAdminView)
