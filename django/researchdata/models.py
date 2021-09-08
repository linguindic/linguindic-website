from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Upper
from . import apps
from django.urls import reverse


# Common functions

def dynamic_citation_author(self):
    # Use manually specified author, if given
    if self.meta_citation_author is not None:
        first_name = self.meta_citation_author.first_name
        last_name = self.meta_citation_author.last_name
    # Or use last updated by
    elif self.meta_lastupdated_by is not None:
        first_name = self.meta_lastupdated_by.first_name
        last_name = self.meta_lastupdated_by.last_name
    # Or use created by
    else:
        first_name = self.meta_created_by.first_name
        last_name = self.meta_created_by.last_name

    return "{}, {}".format(last_name, first_name)


def description_preview(description):
    max_len = 200
    if len(description) > max_len:
        return "{}...".format(description[:max_len - 3].strip())
    else:
        return description


# Select List models


class SlLinguisticTraditionGroup(models.Model):
    """
    Select List table: a group of linguistic traditions (as defined in LinguisticTradition model)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name="sllinguistictraditiongroup_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="sllinguistictraditiongroup_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A group of linguistic traditions"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_sl_linguistictraditiongroup".format(apps.app_name)


class SlReferencePublisher(models.Model):
    """
    Select List table: the publisher of a material being referenced
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name="slreferencepublisher_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="slreferencepublisher_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A publisher"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_sl_referencepublisher".format(apps.app_name)


class SlReferenceType(models.Model):
    """
    Select List table: a type of material being referenced (e.g. a book, website, journal)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name="slreferencetype_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="slreferencetype_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name.title()

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A type of reference"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_sl_referencetype".format(apps.app_name)


class SlTextGroup(models.Model):
    """
    Select List table: a group of texts (as defined in Text model)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name="sltextgroup_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="sltextgroup_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A group of texts"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_sl_textgroup".format(apps.app_name)


class SlTextType(models.Model):
    """
    Select List table: the types of texts (as defined in Text model)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name="sltexttype_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="sltexttype_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A type of text"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_sl_texttype".format(apps.app_name)


# Main models

# Most main models have many to many (m2m) relationships with each other.
# (There may be a few exceptions, e.g. Text and TextPassage share a one-to-many relationship, as TextPassage is a subset of Text)
# As m2m relationships are just defined in 1 of the 2 related models (e.g. the relationship isn't defined in both)
# the 2nd model (in alphabetical order) is the one that contains the relationship.
# E.g. author_text is stored in Text model, not Author.


class Author(models.Model):
    """
    People who have authored works, including those from both modern Western and ancient Indian traditions
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    alternative_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location_most_active = models.CharField(max_length=255, blank=True, null=True)
    date_active = models.CharField(max_length=255, blank=True, null=True)
    # Many to many relationship fields
    related_name = "author"
    author = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_author_author".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="author_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="author_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="author_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        if self.name:
            return self.name
        elif self.alternative_name:
            return self.alternative_name
        else:
            return "(Unnamed author)"

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        subtitle = "An author"
        if self.location_most_active:
            subtitle += " from {}".format(self.location_most_active)
        if self.date_active:
            subtitle += ". Active {}".format(self.date_active)
        return subtitle

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-authors-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_author".format(apps.app_name)
        ordering = [Upper('name'), Upper('alternative_name'), 'id']


class LinguisticField(models.Model):
    """
    The area of linguistics, e.g. syntax, semantics, morphology, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Many to many relationship fields
    related_name = "linguistic_field"
    linguistic_field = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_linguisticfield_linguisticfield".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_linguisticfield".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="linguisticfield_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="linguisticfield_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="linguisticfield_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A linguistic field"

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-linguisticfields-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_linguisticfield".format(apps.app_name)
        ordering = [Upper('name'), Upper('description'), 'id']


class LinguisticNotion(models.Model):
    """
    The main data being collected.
    A series of linguistic ideas/notions/concepts from different traditions that can be mapped to one another
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Many to many relationship fields
    related_name = "linguistic_notion"
    linguistic_notion = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_linguisticnotion_linguisticnotion".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_linguisticnotion".format(apps.app_name))
    linguistic_field = models.ManyToManyField("LinguisticField", related_name=related_name, blank=True,
                                              db_table="{}_m2m_linguisticfield_linguisticnotion".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="linguisticnotion_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="linguisticnotion_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="linguisticnotion_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A linguistic notion"

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-linguisticnotions-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_linguisticnotion".format(apps.app_name)
        ordering = [Upper('name'), Upper('description'), 'id']


class LinguisticTradition(models.Model):
    """
    A specific linguistic tradition, which can be grouped by SlLinguisticTraditionGroup
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # Foreign key fields
    linguistic_tradition_group = models.ForeignKey(SlLinguisticTraditionGroup,
                                                   on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    related_name = "linguistic_tradition"
    linguistic_tradition = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_linguistictradition_linguistictradition".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_linguistictradition".format(apps.app_name))
    linguistic_field = models.ManyToManyField("LinguisticField", related_name=related_name, blank=True,
                                              db_table="{}_m2m_linguisticfield_linguistictradition".format(apps.app_name))
    linguistic_notion = models.ManyToManyField("LinguisticNotion", related_name=related_name, blank=True,
                                               db_table="{}_m2m_linguisticnotion_linguistictradition".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="linguistictradition_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="linguistictradition_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="linguistictradition_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A linguistic tradition"

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-linguistictraditions-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_linguistictradition".format(apps.app_name)
        ordering = [Upper('name'), Upper('description'), 'id']


class Reference(models.Model):
    """
    Information about pieces of work, so that these pieces of work can be properly referenced in the project
    """
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    authors_list = models.CharField(max_length=255, blank=True, null=True)
    editors = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    book_title = models.CharField(max_length=255, blank=True, null=True)
    journal_title = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    page_start = models.CharField(max_length=255, blank=True, null=True)
    page_end = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    public_notes = models.TextField(blank=True, null=True)
    last_accessed_date = models.CharField(max_length=255, blank=True, null=True)
    # Foreign key fields
    reference_type = models.ForeignKey(SlReferenceType, on_delete=models.SET_NULL, blank=True, null=True)
    reference_publisher = models.ForeignKey(SlReferencePublisher, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    related_name = "reference"
    reference = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_reference_reference".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_reference".format(apps.app_name))
    linguistic_field = models.ManyToManyField("LinguisticField", related_name=related_name, blank=True,
                                              db_table="{}_m2m_linguisticfield_reference".format(apps.app_name))
    linguistic_notion = models.ManyToManyField("LinguisticNotion", related_name=related_name, blank=True,
                                               db_table="{}_m2m_linguisticnotion_reference".format(apps.app_name))
    linguistic_tradition = models.ManyToManyField("LinguisticTradition", related_name=related_name, blank=True,
                                                  db_table="{}_m2m_linguistictradition_reference".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="reference_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="reference_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="reference_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.dynamic_summary

    @property
    def dynamic_subtitle(self):
        return self.reference_type.name.title()

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    @property
    def dynamic_summary(self):

        # Book
        if self.reference_type == SlReferenceType.objects.get(name='book'):
            ref = "{authors} ({year}), <em>{title}.".format(authors=self.authors_list,
                                                            year=self.year,
                                                            title=self.title)
            if self.subtitle:
                ref += " {}.".format(self.subtitle)
            ref += "</em> {}: {}.".format(self.location, self.reference_publisher)
            if self.url:
                ref += " {}.".format(self.url)

        # Paper in Edited Volume
        elif self.reference_type == SlReferenceType.objects.get(name='paper in edited volume'):
            ref = "{authors} ({year}), '{title}.".format(authors=self.authors_list, year=self.year, title=self.title)
            if self.subtitle:
                ref += " {}.".format(self.subtitle)
            ref += "' In {} (ed.), <em>{}</em>, {}-{}. {}: {}.".format(self.editors,
                                                                       self.book_title,
                                                                       self.page_start,
                                                                       self.page_end,
                                                                       self.location,
                                                                       self.reference_publisher)
            if self.url:
                ref += " {}.".format(self.url)

        # Journal Article
        elif self.reference_type == SlReferenceType.objects.get(name='journal article'):
            ref = "{authors} ({year}), '{title}'.".format(authors=self.authors_list,
                                                          year=self.year,
                                                          title=self.title)
            if self.subtitle:
                ref += " {}.".format(self.subtitle)
            ref += " <em>{}</em> {}".format(self.journal_title, self.volume)
            if self.number:
                ref += " ({})".format(self.number)
            ref += ": {}-{}.".format(self.page_start, self.page_end)
            if self.url:
                ref += " {}.".format(self.url)

        # PhD Thesis
        elif self.reference_type == SlReferenceType.objects.get(name='phd thesis'):
            ref = "{authors} ({year}), '{title}'.".format(authors=self.authors_list,
                                                          year=self.year,
                                                          title=self.title)
            if self.subtitle:
                ref += " {}.".format(self.subtitle)
            ref += "' PhD thesis, {}.".format(self.school)
            if self.url:
                ref += " {}.".format(self.url)

        # Edited volume
        elif self.reference_type == SlReferenceType.objects.get(name='edited volume'):
            ref = "{editors} (ed.) ({year}), <em>{title}.".format(editors=self.editors,
                                                                  year=self.year,
                                                                  title=self.title)
            if self.subtitle:
                ref += " {}.".format(self.subtitle)
            ref += "</em> {}: {}.".format(self.location, self.reference_publisher)
            if self.url:
                ref += " {}.".format(self.url)

        # Miscellaneous Author (year), title. Public notes.
        elif self.reference_type == SlReferenceType.objects.get(name='miscellaneous'):
            ref = "{authors} ({year}), {title}.".format(authors=self.authors_list,
                                                        year=self.year,
                                                        title=self.title)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)

        # If none of above reference types
        else:
            ref = "{authors} ({year}), '{title}'.".format(authors=self.authors_list,
                                                          year=self.year,
                                                          title=self.title)
            if self.subtitle:
                ref += " {}.".format(self.subtitle)
            if self.url:
                ref += " {}.".format(self.url)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)

        return ref

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-references-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_reference".format(apps.app_name)
        ordering = [Upper('reference_type__name'),
                    Upper('authors_list'),
                    Upper('editors'),
                    Upper('title'), 'id']


class SanskritWord(models.Model):
    """
    A series of words from the Indian language of Sanskrit
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Many to many relationship fields
    related_name = "sanskrit_word"
    sanskrit_word = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_sanskritword_sanskritword".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_sanskritword".format(apps.app_name))
    linguistic_field = models.ManyToManyField("LinguisticField", related_name=related_name, blank=True,
                                              db_table="{}_m2m_linguisticfield_sanskritword".format(apps.app_name))
    linguistic_notion = models.ManyToManyField("LinguisticNotion", related_name=related_name, blank=True,
                                               db_table="{}_m2m_linguisticnotion_sanskritword".format(apps.app_name))
    linguistic_tradition = models.ManyToManyField("LinguisticTradition", related_name=related_name, blank=True,
                                                  db_table="{}_m2m_linguistictradition_sanskritword".format(apps.app_name))
    reference = models.ManyToManyField("Reference", related_name=related_name, blank=True, db_table="{}_m2m_reference_sanskritword".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="sanskritword_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="sanskritword_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="sanskritword_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        return "A Sanskrit word/form"

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-sanskritwords-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_sanskritword".format(apps.app_name)
        ordering = [Upper('name'), Upper('description'), 'id']


class Text(models.Model):
    """
    Pieces of text, primarily from ancient Indian tradition, e.g. books, manuscripts

    This has a one-to-many relationship with TextPassage model,
    rather than many-to-many like most other main tables have with one another
    """
    name = models.CharField(max_length=100)
    alternative_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    approximate_date_of_creation = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    author_main = models.CharField(max_length=255, blank=True, null=True, verbose_name="Author")
    # Foreign key fields
    text_group = models.ForeignKey(SlTextGroup, on_delete=models.SET_NULL, blank=True, null=True)
    text_type = models.ForeignKey(SlTextType, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    related_name = "text"
    text = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_text_text".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_text".format(apps.app_name))
    linguistic_field = models.ManyToManyField("LinguisticField", related_name=related_name, blank=True,
                                              db_table="{}_m2m_linguisticfield_text".format(apps.app_name))
    linguistic_notion = models.ManyToManyField("LinguisticNotion", related_name=related_name, blank=True,
                                               db_table="{}_m2m_linguisticnotion_text".format(apps.app_name))
    linguistic_tradition = models.ManyToManyField("LinguisticTradition", related_name=related_name, blank=True,
                                                  db_table="{}_m2m_linguistictradition_text".format(apps.app_name))
    reference = models.ManyToManyField("Reference", related_name=related_name, blank=True, db_table="{}_m2m_reference_text".format(apps.app_name))
    sanskrit_word = models.ManyToManyField("SanskritWord", related_name=related_name, blank=True, db_table="{}_m2m_sanskritword_text".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="text_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="text_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="text_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        if self.name:
            return self.name
        elif self.alternative_name:
            return self.alternative_name
        else:
            return '(Unnamed text)'

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        elif self.text_group:
            return "A text from {}".format(self.text_group)
        elif self.text_type:
            return "A text of type: {}".format(self.text_type)
        else:
            return "A piece of text"

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-texts-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_text".format(apps.app_name)
        ordering = [Upper('name'), Upper('alternative_name'), 'id']


class TextPassage(models.Model):
    """
    Specific passages of texts

    This has a one-to-many relationship with Text model,
    rather than many-to-many like most other main tables have with one another
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Foreign key fields
    text = models.ForeignKey(Text, on_delete=models.PROTECT)
    text_type = models.ForeignKey(SlTextType, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    related_name = "text_passage"
    text_passage = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_textpassage_textpassage".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_textpassage".format(apps.app_name))
    linguistic_field = models.ManyToManyField("LinguisticField", related_name=related_name, blank=True,
                                              db_table="{}_m2m_linguisticfield_textpassage".format(apps.app_name))
    linguistic_notion = models.ManyToManyField("LinguisticNotion", related_name=related_name, blank=True,
                                               db_table="{}_m2m_linguisticnotion_textpassage".format(apps.app_name))
    linguistic_tradition = models.ManyToManyField("LinguisticTradition", related_name=related_name, blank=True,
                                                  db_table="{}_m2m_linguistictradition_textpassage".format(apps.app_name))
    reference = models.ManyToManyField("Reference", related_name=related_name, blank=True, db_table="{}_m2m_reference_textpassage".format(apps.app_name))
    sanskrit_word = models.ManyToManyField("SanskritWord", related_name=related_name, blank=True, db_table="{}_m2m_sanskritword_textpassage".format(apps.app_name))
    # no m2m relationship with Text as this is a one-to-many relationship, so a FK field called 'text' above in this model
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_citation_author = models.ForeignKey(User, related_name="textpassage_citation_author",
                                             on_delete=models.PROTECT, blank=True, null=True, verbose_name="Author (in citation)")
    meta_created_by = models.ForeignKey(User, related_name="textpassage_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="textpassage_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.description:
            return description_preview(self.description)
        elif self.text:
            return "From the text: {}".format(self.text)
        else:
            return "A text passage"

    @property
    def dynamic_citation_author(self):
        return dynamic_citation_author(self)

    def __str__(self):
        return self.dynamic_title

    def get_absolute_url(self):
        return reverse('browse-textpassages-detail', args=[str(self.id)])

    class Meta:
        db_table = "{}_main_textpassage".format(apps.app_name)
        ordering = [Upper('name'), Upper('description'), 'id']
