from django.db import models
from django.contrib.auth.models import User
from . import apps


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

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
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

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
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

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
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

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
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

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
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
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
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
    meta_created_by = models.ForeignKey(User, related_name="author_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="author_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        if self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        elif self.alternative_name:
            return self.alternative_name
        else:
            return "(Unnamed author)"

    @property
    def dynamic_subtitle(self):
        subtitle = "An author"
        if self.location_most_active:
            subtitle += " from {}".format(self.location_most_active)
        if self.date_active:
            subtitle += ". Active {}".format(self.date_active)
        return subtitle

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_author".format(apps.app_name)


class LinguisticField(models.Model):
    """
    The area of linguistics, e.g. syntax, semantics, morphology, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Many to many relationship fields
    related_name = "linguisticfield"
    linguistic_field = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_linguisticfield_linguisticfield".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_linguisticfield".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name="linguisticfield_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="linguisticfield_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        return "A linguistic field"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_linguisticfield".format(apps.app_name)


class LinguisticNotion(models.Model):
    """
    The main data being collected.
    A series of linguistic ideas/notions/concepts from different traditions that can be mapped to one another
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Many to many relationship fields
    related_name = "linguisticnotion"
    linguistic_notion = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_linguisticnotion_linguisticnotion".format(apps.app_name))
    author = models.ManyToManyField("Author", related_name=related_name, blank=True, db_table="{}_m2m_author_linguisticnotion".format(apps.app_name))
    linguistic_field = models.ManyToManyField("LinguisticField", related_name=related_name, blank=True,
                                              db_table="{}_m2m_linguisticfield_linguisticnotion".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name="linguisticnotion_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="linguisticnotion_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        return "A linguistic notion"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_linguisticnotion".format(apps.app_name)


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
    related_name = "linguistictradition"
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
    meta_created_by = models.ForeignKey(User, related_name="linguistictradition_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="linguistictradition_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        return "A linguistic tradition"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_linguistictradition".format(apps.app_name)


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
    meta_created_by = models.ForeignKey(User, related_name="reference_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="reference_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        if self.title:
            return self.title
        elif self.book_title:
            return self.book_title
        elif self.journal_title:
            return self.journal_title
        elif self.url:
            return self.url
        else:
            return "(Unnamed reference)"

    @property
    def dynamic_subtitle(self):
        return "A {} reference --- {}".format(self.reference_type.name, self.dynamic_summary)

    @property
    def dynamic_summary(self):

        # Book
        if self.reference_type == SlReferenceType.objects.get(name='book'):
            ref = "{authors} ({year}), <em>{title}</em>. {location}: {publisher}.".format(authors=self.authors_list,
                                                                                          year=self.year,
                                                                                          title=self.title,
                                                                                          location=self.location,
                                                                                          publisher=self.reference_publisher)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)
            if self.url:
                ref += " {}.".format(self.url)

        # Paper in Edited Volume
        elif self.reference_type == SlReferenceType.objects.get(name='paper in edited volume'):
            ref = "{authors} ({year}), '{title}'. In {editors} (ed.), <em>{book}</em>, \
                   {page_start}-{page_end}. {location}: {publisher}.".format(authors=self.authors_list,
                                                                             year=self.year,
                                                                             title=self.title,
                                                                             editors=self.editors,
                                                                             book=self.book_title,
                                                                             page_start=self.page_start,
                                                                             page_end=self.page_end,
                                                                             location=self.location,
                                                                             publisher=self.reference_publisher)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)
            if self.url:
                ref += " {}.".format(self.url)

        # Journal Article
        elif self.reference_type == SlReferenceType.objects.get(name='journal article'):
            ref = "{authors} ({year}), '{title}'. <em>{journal}</em> {volume}".format(authors=self.authors_list,
                                                                                      year=self.year,
                                                                                      title=self.title,
                                                                                      journal=self.journal_title,
                                                                                      volume=self.volume)
            if self.number:
                ref += "({})".format(self.number)
            ref += ": {}-{}.".format(self.page_start, self.page_end)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)
            if self.url:
                ref += " {}.".format(self.url)

        # PhD Thesiss
        elif self.reference_type == SlReferenceType.objects.get(name='phd thesis'):
            ref = "{authors} ({year}), '{title}'. PhD thesis, {school}".format(authors=self.authors_list,
                                                                               year=self.year,
                                                                               title=self.title,
                                                                               school=self.school)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)
            if self.url:
                ref += " {}.".format(self.url)

        # Edited volume
        if self.reference_type == SlReferenceType.objects.get(name='edited volume'):
            ref = "{editors} (ed.) ({year}), <em>{title}</em>. {location}: {publisher}.".format(editors=self.editors,
                                                                                                year=self.year,
                                                                                                title=self.title,
                                                                                                location=self.location,
                                                                                                publisher=self.reference_publisher)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)
            if self.url:
                ref += " {}.".format(self.url)

        # If none of above reference types
        else:
            ref = "{authors} ({year}), '{title}'.".format(authors=self.authors_list,
                                                          year=self.year,
                                                          title=self.title)
            if self.public_notes:
                ref += " {}.".format(self.public_notes)
            if self.url:
                ref += " {}.".format(self.url)

        return ref

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_reference".format(apps.app_name)


class SanskritWord(models.Model):
    """
    A series of words from the Indian language of Sanskrit
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Many to many relationship fields
    related_name = "sanskritword"
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
    meta_created_by = models.ForeignKey(User, related_name="sanskritword_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="sanskritword_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        return "A word in the language of Sanskrit"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_sanskritword".format(apps.app_name)


class Text(models.Model):
    """
    Pieces of text, primarily from ancient Indian tradition, e.g. books, manuscripts

    This has a one-to-many relationship with TextPassage model,
    rather than many-to-many like most other main tables have with one another
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    approximate_date_of_creation = models.CharField(max_length=200, blank=True, null=True)
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
    meta_created_by = models.ForeignKey(User, related_name="text_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="text_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.text_group:
            return "A text from {}".format(self.text_group)
        elif self.text_type:
            return "A text of type: {}".format(self.text_type)
        else:
            return "A text"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_text".format(apps.app_name)


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
    related_name = "textpassage"
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
    meta_created_by = models.ForeignKey(User, related_name="textpassage_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_by = models.ForeignKey(User, related_name="textpassage_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def dynamic_title(self):
        return self.name

    @property
    def dynamic_subtitle(self):
        if self.text:
            return "A passage of text from {}".format(self.text)
        elif self.text_type:
            return "A passage of {} text".format(self.text_type)
        else:
            return "A passage of text"

    def __str__(self):
        return self.dynamic_title

    class Meta:
        db_table = "{}_main_textpassage".format(apps.app_name)
