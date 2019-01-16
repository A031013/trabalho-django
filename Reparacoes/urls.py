from django.urls import path
from . import views

urlpatterns = [
    path('', views.reparacao_lista, name='reparacao_lista'),
	path('reparar/<int:pk>/', views.reparar, name='reparar'),
	path('pecas', views.peca_lista, name='peca_lista'),
	path('pecas/nova', views.peca_nova, name='peca_nova'),
	path('stock', views.stock, name='stock'),
	path('stock/retirar', views.stock_retirar, name='stock_retirar'),
	path('encomendas', views.encomenda_lista, name='encomenda_lista'),
	path('encomendar', views.encomendar, name='encomendar'),
	path('encomenda/entrada/<int:pk>/', views.encomenda_entrada, name='encomenda_entrada'),
	path('fornecedores', views.fornecedor_lista, name='fornecedor_lista'),
	path('fornecedores/novo', views.fornecedor_novo, name='fornecedor_novo'),
	
]