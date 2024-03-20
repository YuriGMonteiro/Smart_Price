from django.shortcuts import render
from .forms import RegisterForm


import time
import pandas as pd
# import Preco_mercado
import warnings
import requests
# import Quantidade_Vendida
# import DadosBling



# BLING_SECRET_KEY = "07bd3fa38742e5b5edb6b795d30858d4260742412046e74d44b0b2fc227daacf3e75261a"


def user_register(request):
    context = {}
    context['cadastro_usuario'] = RegisterForm
    
    if request.method == "POST":
        registro_usuario = RegisterForm(request.POST)
        if registro_usuario.is_valid():
            user = registro_usuario.save(commit=False)
            user.username = user.email
            user.save()
    return render(request, "pages/register.html", context=context)

def list_all_products(request):
    if request.user.is_authenticated:
        page = 1
        all_products = []
        BLING_SECRET_KEY = request.user.token   

    while True:
        url = f'https://bling.com.br/Api/v2/produtos/page={page}/json/'
        payload = {'apikey': BLING_SECRET_KEY, 'estoque': 'S'}

        produtos = requests.get(url, params=payload)

        try:
            pagina = produtos.json().get('retorno', {}).get('produtos', [])
            if not pagina:
                break
            all_products.extend(pagina)
            page += 1
        except KeyError:
            break

    return all_products
    
def home(request):
    
    dados_produtos = []
    
    produtos = list_all_products(request)
    
    for produto in produtos[:10]:  # Limitando para os 10 primeiros produtos
        produto_info = produto.get('produto', {})
        dados_produtos.append({
            'id': produto_info.get('id', ''),
            'Codigo': produto_info.get('codigo', ''),
            'Descricao': produto_info.get('descricao', ''),
            'Situacao': produto_info.get('situacao', ''),
            'Preco': float(produto_info.get('preco', '0.0')),
            'PrecoCusto': float(produto_info.get('precoCusto', '0.0')) if produto_info.get('precoCusto') else None,
            'EstoqueAtual': int(produto_info.get('estoqueAtual', '0'))
        })

    context = {}
    context['produtos'] =  dados_produtos

    
    return render(request, "pages/home.html", context=context)
