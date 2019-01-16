from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Reparacao(models.Model):
	equipamento = models.CharField(max_length=200)
	numero_serie = models.CharField(max_length=200)
	avaria = models.TextField()
	aguarda_encomenda = models.BooleanField(default=False)
	preco = models.FloatField(null=True, blank=True, default=None)
	estado_escolhas = (
		("Em Analise","Em Analise"),  
		("Arranjado","Arranjado"),
	)
	estado = models.CharField(choices=estado_escolhas, max_length=20)
	arranjo = models.TextField(null=True, blank=True, default=None)
	def publish(self):
		self.save()	
	def __str__(self):
		return self.equipamento
		
class Peca(models.Model):
	nome = models.CharField(max_length=200)
	marca = models.CharField(max_length=200)
	preco = models.FloatField(null=True, blank=True, default=None)
	def publish(self):
		self.save()
	def __str__(self):
		return self.nome
		
class Stock(models.Model):
	nome_peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
	quantidade = models.IntegerField(null=False, default=0)
	def publish(self):
		self.save()
	def __str__(self):
		return self.nome_peca
		
class Fornecedor(models.Model):
	nome = models.CharField(max_length=200, null=False)
	localidade = models.CharField(max_length=30)
	morada = models.CharField(max_length=200)
	def publish(self):
		self.save()
	def __str__(self):
		return self.nome
		

class Encomenda(models.Model):
	fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
	nome_peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
	quantidade = models.IntegerField(null=False, default=1)
	entregue = models.BooleanField(default=False)
	data = models.DateTimeField(null=False)
	def publish(self):
		self.save()
	def __str__(self):
		return self.nome_peca.nome
	
	
	
