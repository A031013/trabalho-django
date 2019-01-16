from django.contrib import admin
from .models import Reparacao, Peca, Encomenda, Fornecedor, Stock

admin.site.register(Reparacao)
admin.site.register(Peca)
admin.site.register(Encomenda)
admin.site.register(Fornecedor)
admin.site.register(Stock)
