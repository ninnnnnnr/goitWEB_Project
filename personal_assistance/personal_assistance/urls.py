from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('file_manager/', include('file_manager.urls')),
    path('notes/', include('notes.urls')),
    path('adress_book/', include('adress_book.urls')),
    path('', include("news.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
