from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # For language switcher
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('markdownx/', include('markdownx.urls')),
    path('', include('landing_page.urls', namespace='landing_page')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('photos/', include('photos.urls', namespace='photos')),
    path('things-to-do/', include('things_to_do.urls', namespace='things_to_do')),
    path("__reload__/", include("django_browser_reload.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)