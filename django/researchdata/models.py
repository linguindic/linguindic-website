from django.db import models
from django.contrib.auth.models import User
from . import apps


# Select List models


class SlLinguisticNotionsRelationshipType(models.Model):
    """
    Select List table: the types of relationships between 2 linguistic notions
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='sllinguisticnotionsrelationshiptype_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='sllinguisticnotionsrelationshiptype_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "{}_sl_linguisticnotionsrelationshiptype".format(apps.app_name)


class SlLinguisticTraditionGroup(models.Model):
    """
    Select List table: a group of linguistic traditions (as defined in SlLinguisticTradition model)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='sllinguistictraditiongroup_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='sllinguistictraditiongroup_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "{}_sl_linguistictraditiongroup".format(apps.app_name)


class SlLinguisticTradition(models.Model):
    """
    Select List table: a specific linguistic tradition, which can be grouped by SlLinguisticTraditionGroup
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # Foreign key fields
    linguistic_tradition_group = models.ForeignKey(SlLinguisticTraditionGroup,
                                                   on_delete=models.SET_NULL, blank=True, null=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='sllinguistictradition_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='sllinguistictradition_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "{}_sl_linguistictradition".format(apps.app_name)


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
    meta_created_by = models.ForeignKey(User, related_name='slreferencepublisher_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='slreferencepublisher_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

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
    meta_created_by = models.ForeignKey(User, related_name='slreferencetype_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='slreferencetype_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

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
    meta_created_by = models.ForeignKey(User, related_name='sltextgroup_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='sltextgroup_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

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
    meta_created_by = models.ForeignKey(User, related_name='sltexttype_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='sltexttype_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "{}_sl_texttype".format(apps.app_name)


# Main models


class Reference(models.Model):
    """
    Information about pieces of work, so that these pieces of work can be properly referenced in the project
    """
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    editors = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    edition = models.CharField(max_length=255, blank=True, null=True)
    book_title = models.CharField(max_length=255, blank=True, null=True)
    journal_title = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    page_start = models.CharField(max_length=255, blank=True, null=True)
    page_end = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    last_accessed_date = models.CharField(max_length=255, blank=True, null=True)
    # Foreign key fields
    reference_type = models.ForeignKey(SlReferenceType, on_delete=models.SET_NULL, blank=True, null=True)
    reference_publisher = models.ForeignKey(SlReferencePublisher, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    # (relationships specified in other models: Text, Author, LinguisticNotion. See 'related_name' value in each.)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='reference_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='reference_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
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
    def details(self):
        return "Details"

    class Meta:
        db_table = "{}_main_reference".format(apps.app_name)


class Text(models.Model):
    """
    Pieces of text, primarily from ancient Indian tradition, e.g. books, manuscripts
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    approximate_date_of_creation = models.CharField(max_length=200, blank=True, null=True)
    # Foreign key fields
    text_group = models.ForeignKey(SlTextGroup, on_delete=models.SET_NULL, blank=True, null=True)
    text_type = models.ForeignKey(SlTextType, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    # (relationships specified in other models: Author, LinguisticNotion. See 'related_name' value in each.)
    related_name = 'text'
    reference = models.ManyToManyField(Reference, related_name=related_name, blank=True, db_table="{}_m2m_text_reference".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='text_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='text_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name
    
    @property
    def details(self):
        return "Details"

    class Meta:
        db_table = "{}_main_text".format(apps.app_name)


class Author(models.Model):
    """
    People who have authored works, including those from both modern Western and ancient Indian traditions
    """
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    alternative_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location_most_active = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    # Foreign key fields
    linguistic_tradition = models.ForeignKey(SlLinguisticTradition, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    # (relationships specified in other models: LinguisticNotion. See 'related_name' value in each.)
    related_name = 'author'
    text = models.ManyToManyField(Text, related_name=related_name, blank=True, db_table="{}_m2m_author_text".format(apps.app_name))
    reference = models.ManyToManyField(Reference, related_name=related_name, blank=True, db_table="{}_m2m_author_reference".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='author_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='author_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
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
    def details(self):
        return "Details"

    class Meta:
        db_table = "{}_main_author".format(apps.app_name)


class LinguisticField(models.Model):
    """
    The area of linguistics, e.g. syntax, semantics, morphology, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Many to many relationship fields
    # (relationships specified in other models: LinguisticNotion. See 'related_name' value in each.)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='linguisticfield_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='linguisticfield_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name
    
    @property
    def details(self):
        return "Details"

    class Meta:
        db_table = "{}_main_linguisticfield".format(apps.app_name)


class LinguisticNotion(models.Model):
    """
    The main data being collected.
    A series of linguistic ideas/notions/concepts from different traditions that can be mapped to one another
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    star_count = models.IntegerField(default=0)
    # Many to many relationship fields
    related_name = 'linguistic_notion'
    author = models.ManyToManyField(Author, related_name=related_name, blank=True, db_table="{}_m2m_author_linguisticnotion".format(apps.app_name))
    linguisticfield = models.ManyToManyField(LinguisticField, related_name=related_name, blank=True,
                                             db_table="{}_m2m_linguisticfield_linguisticnotion".format(apps.app_name))
    reference = models.ManyToManyField(Reference, related_name=related_name, blank=True, db_table="{}_m2m_linguisticnotion_reference".format(apps.app_name))
    text = models.ManyToManyField(Text, related_name=related_name, blank=True, db_table="{}_m2m_linguisticnotion_text".format(apps.app_name))
    linguistic_notion = models.ManyToManyField("self", through="M2MLinguisticNotionsRelationship")
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_by = models.ForeignKey(User, related_name='linguisticnotion_created_by',
                                        on_delete=models.PROTECT, blank=True, null=True)
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_by = models.ForeignKey(User, related_name='linguisticnotion_lastupdated_by',
                                            on_delete=models.PROTECT, blank=True, null=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name
    
    @property
    def details(self):
        if self.description:
            return self.description
        elif self.example:
            return "E.g. {}".format(self.description)

    class Meta:
        db_table = "{}_main_linguisticnotion".format(apps.app_name)


# Many to Many tables

class M2MLinguisticNotionsRelationship(models.Model):
    """
    Many to many relationship between 2 linguistic notions (LinguisticNotion model with itself)
    """
    linguistic_notion_1 = models.ForeignKey(LinguisticNotion, related_name="linguistic_notion_1", on_delete=models.CASCADE)
    linguistic_notion_2 = models.ForeignKey(LinguisticNotion, related_name="linguistic_notion_2", on_delete=models.CASCADE)
    # Foreign key fields
    linguistic_notions_relationship_type = models.ForeignKey(SlLinguisticNotionsRelationshipType, on_delete=models.PROTECT)

    class Meta:
        db_table = "{}_m2m_linguisticnotions".format(apps.app_name)
