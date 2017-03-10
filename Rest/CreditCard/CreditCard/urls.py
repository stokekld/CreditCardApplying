"""CreditCard URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers
from usuario.views import UsuarioViewSet
# from django.contrib import admin
# from usuario.urls import router


router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet, 'usuarios')
urlpatterns = router.urls

# urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^auth', include('usuario.urls')),
    # url(r'^usuarios', include('usuario.urls')),
    # url(r'^', include('usuario.urls')),
    # url(r'^', include('rest_framework.urls')),
# ]
