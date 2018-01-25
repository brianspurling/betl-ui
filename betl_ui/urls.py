"""betl_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # The include() function allows referencing other URLconfs. Whenever Django
    # encounters include(), it chops off whatever part of the URL matched up to
    # that point and sends the remaining string to the included URLconf for
    #further processing.
    path('console/', include('console.urls')),
    path('admin/', admin.site.urls),
]
