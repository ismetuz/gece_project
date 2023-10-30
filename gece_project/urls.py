"""
URL configuration for gece_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from page_app.views import home_view,category_view,all_products, about_us, contact_us
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('tum_urunler/',all_products, name='tum_urunler'),
    path('<slug:category_slug>',category_view, name='category_view'),
    path('about_us/',about_us, name='about_us'),
    path('contact_us/',contact_us, name='contact_us'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
