"""voylla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from django.urls import path

from django.conf import settings
from django.conf.urls import url
from jewellery import views

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', name="index"),
    url('admin/', admin.site.urls),
    #path('upload/', views.upload, name='upload'),
    #url(r'^admin/$', admin.site.urls),
    url('saved/', views.upload, name='upload'),
    url('upload/', views.upload_form, name='upload_form'),
    url('saved/next', views.next, name='get_form'),
    url('csv/',views.csv_dict_reader,name='insert'),
    url('jewellery/',views.display_jew,name='display_jew'),
    url('webcam/',views.webcam,name='webcam'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
