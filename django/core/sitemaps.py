from django.contrib.sitemaps import Sitemap
from researchdata import models
from django.urls import reverse


class StaticPagesSitemap(Sitemap):
    """
    Sitemap: Static pages (e.g. support, cookies, api)
    """

    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return ['welcome',
                'about-project',
                'about-team',
                'about-funding',
                'about-events',
                'about-outputs',
                'help',
                'cookies',
                'accessibility']

    def location(self, obj):
        return reverse(obj)


class AuthorListSitemap(Sitemap):
    """
    Sitemap: Author List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-authors-list']

    def lastmod(self, obj):
        try:
            return models.Author.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class AuthorDetailSitemap(Sitemap):
    """
    Sitemap: Author Detail
    """

    priority = 0.9

    def items(self):
        return models.Author.objects.filter(admin_published=True)


class LinguisticFieldListSitemap(Sitemap):
    """
    Sitemap: LinguisticField List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-linguisticfields-list']

    def lastmod(self, obj):
        try:
            return models.LinguisticField.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class LinguisticFieldDetailSitemap(Sitemap):
    """
    Sitemap: LinguisticField Detail
    """

    priority = 0.9

    def items(self):
        return models.LinguisticField.objects.filter(admin_published=True)


class LinguisticNotionListSitemap(Sitemap):
    """
    Sitemap: LinguisticNotion List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-linguisticnotions-list']

    def lastmod(self, obj):
        try:
            return models.LinguisticNotion.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class LinguisticNotionDetailSitemap(Sitemap):
    """
    Sitemap: LinguisticNotion Detail
    """

    priority = 0.9

    def items(self):
        return models.LinguisticNotion.objects.filter(admin_published=True)


class LinguisticTraditionListSitemap(Sitemap):
    """
    Sitemap: LinguisticTradition List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-linguistictraditions-list']

    def lastmod(self, obj):
        try:
            return models.LinguisticTradition.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class LinguisticTraditionDetailSitemap(Sitemap):
    """
    Sitemap: LinguisticTradition Detail
    """

    priority = 0.9

    def items(self):
        return models.LinguisticTradition.objects.filter(admin_published=True)


class ReferenceListSitemap(Sitemap):
    """
    Sitemap: Reference List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-references-list']

    def lastmod(self, obj):
        try:
            return models.Reference.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class ReferenceDetailSitemap(Sitemap):
    """
    Sitemap: Reference Detail
    """

    priority = 0.9

    def items(self):
        return models.Reference.objects.filter(admin_published=True)


class SanskritWordListSitemap(Sitemap):
    """
    Sitemap: SanskritWord List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-sanskritwords-list']

    def lastmod(self, obj):
        try:
            return models.SanskritWord.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class SanskritWordDetailSitemap(Sitemap):
    """
    Sitemap: SanskritWord Detail
    """

    priority = 0.9

    def items(self):
        return models.SanskritWord.objects.filter(admin_published=True)


class TextListSitemap(Sitemap):
    """
    Sitemap: Text List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-texts-list']

    def lastmod(self, obj):
        try:
            return models.Text.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class TextDetailSitemap(Sitemap):
    """
    Sitemap: Text Detail
    """

    priority = 0.9

    def items(self):
        return models.Text.objects.filter(admin_published=True)


class TextPassageListSitemap(Sitemap):
    """
    Sitemap: TextPassage List
    """

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['browse-textpassages-list']

    def lastmod(self, obj):
        try:
            return models.TextPassage.objects.order_by('-meta_created_datetime')[0].meta_created_datetime
        except:
            return None

    def location(self, obj):
        return reverse(obj)


class TextPassageDetailSitemap(Sitemap):
    """
    Sitemap: TextPassage Detail
    """

    priority = 0.9

    def items(self):
        return models.TextPassage.objects.filter(admin_published=True)
