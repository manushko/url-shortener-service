from django.conf.urls import url
from django.contrib import admin

from shortener.views import UrlShortenerDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<short_url>[-\w]+)', UrlShortenerDetailView.as_view())
]
