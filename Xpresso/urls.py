from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from horror_show.sitemaps import PostSitemap


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horror_show/', include('horror_show.urls', namespace='horror_show')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path("", include("horror_show.urls")),
]
