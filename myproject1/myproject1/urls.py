"""myproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pgfansite/', include('pgfansite.urls')),
    path('', TemplateView.as_view(template_name='accounts/home.html'), name='home'), #追加
    path('accounts/', include('allauth.urls')), #追加
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
