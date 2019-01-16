from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Reparacao, Peca, Stock, Fornecedor, Encomenda
from .forms import PecaForm, StockForm, EncomendaForm, EncomendaEntradaForm, FornecedorForm, StockRetirarForm, RepararForm

# Create your views here.
def reparacao_lista(request):
	reparacoes = Reparacao.objects.filter()
	return render(request, 'Reparacoes/reparacao_lista.html', {'reparacoes': reparacoes})
	
def reparar(request, pk):
	reparacao = get_object_or_404(Reparacao, pk=pk)
	if request.method == "POST":
		form = RepararForm(request.POST)
		if form.is_valid():
			reparacao = get_object_or_404(Reparacao, pk=pk)
			reparacao.estado = form.cleaned_data['estado']
			reparacao.preco = form.cleaned_data['preco']
			reparacao.arranjo = form.cleaned_data['arranjo']
			reparacao.aguarda_encomenda = form.cleaned_data['aguarda_encomenda']
			reparacao.save()
			return redirect('reparacao_lista')
	else:
		form = RepararForm()
	return render(request, 'Reparacoes/reparar.html', {'form': form, 'reparacao': reparacao})
	
def peca_lista(request):
	pecas = Peca.objects.filter()
	return render(request, 'Reparacoes/peca_lista.html', {'pecas': pecas})

def fornecedor_lista(request):
	fornecedores = Fornecedor.objects.filter()
	return render(request, 'Reparacoes/fornecedor_lista.html', {'fornecedores': fornecedores})

def fornecedor_novo(request):
	if request.method == "POST":
		form = FornecedorForm(request.POST)
		if form.is_valid():
			fornecedor = form.save(commit=False)
			fornecedor.save()
			return redirect('fornecedor_lista')
	else:
		form = FornecedorForm()
	return render(request, 'Reparacoes/fornecedor_novo.html', {'form': form})
	
def encomenda_lista(request):
	encomendas = Encomenda.objects.filter()
	return render(request, 'Reparacoes/encomenda_lista.html', {'encomendas': encomendas})
	
def encomendar(request):
	if request.method == "POST":
		form = EncomendaForm(request.POST)
		if form.is_valid():
			return redirect('encomenda_lista')
	else:
		form = EncomendaForm()
	return render(request, 'Reparacoes/encomendar.html', {'form': form})

def stock(request):
	stock = Stock.objects.filter()
	return render(request, 'Reparacoes/stock.html', {'stock': stock})

def stock_retirar(request):
	if request.method == "POST":
		form = StockRetirarForm(request.POST)
		if form.is_valid():
			peca = get_object_or_404(Stock, nome_peca=form.cleaned_data['peca'])
			peca.quantidade = peca.quantidade - form.cleaned_data['unidades']
			peca.save()
			return redirect('stock')
	else:
		form = StockRetirarForm()
	return render(request, 'Reparacoes/stock_retirar.html', {'form': form})
	
def encomenda_entrada(request, pk):
	if request.method == "POST":
		form = EncomendaEntradaForm(request.POST, pk)
		if form.is_valid():
			encomenda = get_object_or_404(Encomenda, pk=pk)
			encomenda.entregue = True
			encomenda.save()
			stock = get_object_or_404(Stock, nome_peca=encomenda.nome_peca)
			stock.quantidade = stock.quantidade + encomenda.quantidade
			stock.save()
			return redirect('encomenda_lista')
	else:
		form = EncomendaEntradaForm()
	return render(request, 'Reparacoes/encomenda_entrada.html', {'form': form})

def peca_nova(request):
	if request.method == "POST":
		form = PecaForm(request.POST)
		if form.is_valid():
			peca = form.save(commit=False)
			peca.save()
			peca_procura = get_object_or_404(Peca, nome=peca.nome)
			Stock.objects.create(nome_peca = peca_procura)
			return redirect('peca_lista')
	else:
		form = PecaForm()
	return render(request, 'Reparacoes/peca_edit.html', {'form': form})