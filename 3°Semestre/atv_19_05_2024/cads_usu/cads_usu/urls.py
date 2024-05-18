
from django.contrib import admin
from django.urls import include, path
from app_cad_usuarios import views

urlpatterns = [
    path('', include('app_cad_usuarios.urls')),
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='acesso'),
    path('exibir/',views.exibir,name='exibir'),
    path('curriculo/',views.grafico,name='port'),
    path('cadastro/',views.cadastro,name='cadas'),
    path('cadastrar/',views.cadastrar,name='cadastrando'),
    path('admin/', admin.site.urls),
]