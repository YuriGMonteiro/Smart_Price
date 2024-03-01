from django.shortcuts import render
from .forms import RegisterForm


import time
import pandas as pd
# import Preco_mercado
import warnings
import requests
# import Quantidade_Vendida
# import DadosBling

warnings.simplefilter(
    action='ignore', category=pd.errors.SettingWithCopyWarning)


BLING_SECRET_KEY = "07bd3fa38742e5b5edb6b795d30858d4260742412046e74d44b0b2fc227daacf3e75261a"


def list_all_products(BLING_SECRET_KEY):
    page = 1
    all_products = []

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
    
    produtos = list_all_products(BLING_SECRET_KEY)
    
    for item in produtos[:10]:
        produto = item.get('produto', {})
        codigo = produto.get('codigo', '')
        descricao = produto.get('descricao', '')
        situacao = produto.get('situacao', '')
        preco = float(produto.get('preco', '0.0'))
        precoCusto = float(produto.get('precoCusto', '0.0')) if produto.get('precoCusto') else None
        estoqueAtual = int(produto.get('estoqueAtual', '0'))

        dados_produtos.append({
            'Codigo': codigo,
            'Descricao': descricao,
            'Situacao': situacao,
            'Preco': preco,
            'PrecoCusto': precoCusto,
            'EstoqueAtual': estoqueAtual
        })

    context = {}
    context['produtos'] =  dados_produtos
    # cadastro = RegisterForm()
    # context = {}
    # context['cadastro_usuario'] = cadastro
    
    # if request.method == "POST":
    #     registro_usuario = RegisterForm(request.POST)
    #     if registro_usuario.is_valid():
    #         registro_usuario.save()
    
    return render(request, "pages/home.html", context=context)
