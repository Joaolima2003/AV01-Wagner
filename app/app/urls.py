from django.contrib import admin
from django.urls import path, include
from cadastros.views import listar_cadastros, detalhar_cadastros
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastros/', listar_cadastros),
    path('cadastros/<int:id>/', detalhar_cadastros)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])