"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from registration import views
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import  static
from django.conf import settings




urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/',include('registration.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^api-auth/', include('rest_framework.urls')),

#    url(r'^registerTeamMember/(?P<startup_id>\d+)/$',views.registerTeamMember,name='registerTeamMember'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
