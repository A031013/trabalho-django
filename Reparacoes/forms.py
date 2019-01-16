from django.shortcuts import get_object_or_404
from django import forms
import datetime
from .models import Reparacao, Peca, Stock, Encomenda, Fornecedor
#from django.forms import formset_factory
#RepararFormSet = formset_factory(RepararForm, extra=2)

class PecaForm(forms.ModelForm):
	class Meta:
		model = Peca
		fields = ('nome', 'marca', 'preco')
		
class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ('nome_peca','quantidade')
		
class StockRetirarForm(forms.Form):
	peca = forms.ModelChoiceField(queryset=Peca.objects.all(), required=True)
	unidades = forms.IntegerField(required=True, min_value=1)
	def clean(self):
		cleaned_data = super(StockRetirarForm, self).clean()
		peca = cleaned_data.get('peca')
		unidades = cleaned_data.get('unidades')
		if not peca and not unidades:
			raise forms.ValidationError('É preencher todos os campos !')
			
class FornecedorForm(forms.ModelForm):
	class Meta:
		model = Fornecedor
		fields = ('nome','localidade', 'morada')

class RepararForm(forms.Form):
	preco = forms.IntegerField(required=True, min_value=1)
	estado_escolhas = (
		("Em Analise","Em Analise"),  
		("Arranjado","Arranjado"),
	)
	estado = forms.ChoiceField(choices=estado_escolhas, required=True,)
	arranjo = forms.CharField(widget=forms.Textarea, required=True,)
	aguarda_encomenda = forms.BooleanField(required=False, initial=False, label='Aguarda Encomenda?')

	def clean(self):
		cleaned_data = super(RepararForm, self).clean()
		preco = cleaned_data.get('preco')
		estado = cleaned_data.get('estado')
		arranjo = cleaned_data.get('arranjo')
		aguarda_encomenda = cleaned_data.get('aguarda_encomenda')
	
class EncomendaForm(forms.Form):
	fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all())
	nome_peca = forms.ModelChoiceField(queryset=Peca.objects.all())
	quantidade = forms.IntegerField(min_value=1)
	def clean(self):
		cleaned_data = super(EncomendaForm, self).clean()
		fornecedor = cleaned_data.get('fornecedor')
		nome_peca = cleaned_data.get('nome_peca')
		quantidade = cleaned_data.get('quantidade')
		if not fornecedor and not nome_peca and not quantidade:
			raise forms.ValidationError('Todos os campos são obrigatórios!')
		entregue = False
		data = datetime.datetime.now()
		Encomenda.objects.create( nome_peca = nome_peca,fornecedor = fornecedor, quantidade = quantidade, entregue = entregue, data = data)
		
class EncomendaEntradaForm(forms.Form):
	confirmar = forms.BooleanField(required=True, initial=False, label='Confirmar Entrada')
	def clean(self):
		cleaned_data = super(EncomendaEntradaForm, self).clean()
		confirmar = cleaned_data.get('confirmar')
		if not confirmar:
			raise forms.ValidationError('É necessário confirmar!')
		