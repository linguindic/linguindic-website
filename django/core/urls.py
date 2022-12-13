from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from . import sitemaps

sitemaps = {
    'static-pages': sitemaps.StaticPagesSitemap,

    'browse-authors-list': sitemaps.AuthorListSitemap,
    'browse-authors-detail': sitemaps.AuthorDetailSitemap,

    'browse-linguisticfields-list': sitemaps.LinguisticFieldListSitemap,
    'browse-linguisticfields-detail': sitemaps.LinguisticFieldDetailSitemap,

    'browse-linguisticnotions-list': sitemaps.LinguisticNotionListSitemap,
    'browse-linguisticnotions-detail': sitemaps.LinguisticNotionDetailSitemap,

    'browse-linguistictraditions-list': sitemaps.LinguisticTraditionListSitemap,
    'browse-linguistictraditions-detail': sitemaps.LinguisticTraditionDetailSitemap,

    'browse-references-list': sitemaps.ReferenceListSitemap,
    'browse-references-detail': sitemaps.ReferenceDetailSitemap,

    'browse-sanskritwords-list': sitemaps.SanskritWordListSitemap,
    'browse-sanskritwords-detail': sitemaps.SanskritWordDetailSitemap,

    'browse-texts-list': sitemaps.TextListSitemap,
    'browse-texts-detail': sitemaps.TextDetailSitemap,

    'browse-textpassages-list': sitemaps.TextPassageListSitemap,
    'browse-textpassages-detail': sitemaps.TextPassageDetailSitemap,
}

urlpatterns = [

    # General app's urls
    path('', include('general.urls')),
    # Research Data app's urls
    path('data/', include('researchdata.urls')),
    # Django admin urls
    path('dashboard/', admin.site.urls),
    # Debug Toolbar
    path('__debug__/', include('debug_toolbar.urls')),
    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
