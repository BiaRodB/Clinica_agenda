"""core URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from agenda.views import ClientesViewSet, EspecialidadeViewSet, AgendaMViewSet,ConsultaViewSet, CadastrarViewSet


router = routers.DefaultRouter()
router.register('especialidade',EspecialidadeViewSet)
router.register('cadastrar', CadastrarViewSet)
router.register('agenda', AgendaMViewSet)
router.register('clientes', ClientesViewSet)
router.register('consulta', ConsultaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
   # path(r'^chaining/', include('smart_selects.urls')),

]

