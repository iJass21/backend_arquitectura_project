from django.contrib import admin
from django.urls import path, include
from api.views import health_check
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', health_check),
    path("admin/", admin.site.urls),
    path("api/v1/", include('api.urls')),
    path('docs/', include_docs_urls(title='Api Documentation')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
