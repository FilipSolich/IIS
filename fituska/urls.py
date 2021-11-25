from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.static import serve

from subjects.views import list_subjects


urlpatterns = [
    path('', list_subjects, name='list_subjects'),
    path('subjects/', include('subjects.urls')),
    path('accounts/', include('accounts.urls')),
    path('questions/', include('questions.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Serving media files on Django development server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
