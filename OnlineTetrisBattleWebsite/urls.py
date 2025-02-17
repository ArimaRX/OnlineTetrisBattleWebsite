"""OnlineTetrisBattleWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

handler404 = views.page_not_found_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('', include("registration.urls")),
    path('compete/', include("compete.urls")),
    path('accounts/', include("accounts.urls")),
    path('tournament/', include("tournament.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
