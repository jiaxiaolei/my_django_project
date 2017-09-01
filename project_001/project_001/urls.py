"""project_001 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions

authentication_classes = (SessionAuthentication)
#authentication_classes = (SessionAuthentication, MyBasicAuthentication)
#permission_classes = (IsAuthenticated,)
permission_classes = [permissions.AllowAny]

#import ipdb; ipdb.set_trace();

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('django_rest_swagger_docstring.urls', namespace='docs')),
]
