from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # General app's urls
    path('', include('general.urls')),

    # Research Data app's urls
    path('database/', include('researchdata.urls')),

    # Include Django admin urls
    path('dashboard/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
