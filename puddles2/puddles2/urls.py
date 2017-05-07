"""puddles URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Imports
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

# App internal imports
from puddlesbooking import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^venues/$', views.venues, name='venues'),
    url(r'^availability/$', views.availability, name='availability'),
    url(r'^booking/(?P<id>\d+)/(?P<date>\d{4}-\d{2}-\d{2})/', views.booking, name='booking'),
    url(r'^contact/$', views.contact, name='contact'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)