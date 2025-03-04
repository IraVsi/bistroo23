"""
URL configuration for bistroo project.

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
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_public.urls')),
    path('app_admin/', include('app_admin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', RedirectView.as_view(url='app_public')),  # redirect domain


]

handler500 = 'app_public.views.custom500'
handler404 = 'app_public.views.custom404'