from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cadastros, name='listar_cadastros' ),
    path('<int:id>/', views.detalhar_cadastros , name='detalhar_cadastros'),
]