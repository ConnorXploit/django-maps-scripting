"""djmaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
#from django.utils.translation import gettext_lazy as _
from core.urls import inicio_patterns
from victimas.urls import victimas_patterns
from profiles.urls import profiles_patterns
from scripts.urls import scripts_patterns
from tools.urls import tools_patterns
from messenger.urls import messenger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    # Paths de Home
    path('', include(inicio_patterns)),
    #path(_('admin/'), admin.site.urls),
    path('victimas/', include(victimas_patterns)),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de profiles
    path('scripts/', include(scripts_patterns)),
    # Paths de tools
    path('tools/', include(tools_patterns)),
    # Map
    path('maps/', include('maps.urls')),
    # Paths de messenger
    path('messenger/', include(messenger_patterns)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
