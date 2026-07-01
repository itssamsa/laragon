from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_empleados, name='lista'),
    path('crear/', views.crear_empleado, name='crear'),
]