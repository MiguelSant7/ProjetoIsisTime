from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('registrar_ponto/', views.registrar_ponto, name='registrar_ponto'),
    path('historico/', views.listagem_historico, name='historico'),
    path('home/', views.home, name='home'),
    path('editar_ponto/<int:id>/', views.editar_ponto, name='editar_ponto'),
    path('apagar_ponto/<int:id>/', views.apagar_ponto, name='apagar_ponto'),
]
