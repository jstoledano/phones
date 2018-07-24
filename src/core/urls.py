from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from apps.tracker.views import ReporteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReporteView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
