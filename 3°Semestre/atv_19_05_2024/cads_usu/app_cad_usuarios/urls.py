from django.urls import path
from . import views

app_name = 'app_cad_usuarios'
urlpatterns = [
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
