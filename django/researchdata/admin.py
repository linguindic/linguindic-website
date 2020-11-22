from django.contrib import admin
from . import models


class LinguisticNotionAdminView(admin.ModelAdmin):
    """
    Customise the Linguistic Notion section of the Django admin
    """
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
    ordering = ('id',)


# Register classes
admin.site.register(models.LinguisticNotion, LinguisticNotionAdminView)
