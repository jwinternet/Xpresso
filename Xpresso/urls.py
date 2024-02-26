from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('horror_show/', include('horror_show.urls', namespace='horror_show')),
    path("", include("horror_show.urls"))
]
