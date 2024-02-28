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

def coleta_produtos(produtos):
    dados_produtos = []

    for item in produtos:
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

    df = pd.DataFrame(dados_produtos)
    lista_produtos = df.query('EstoqueAtual > 0 and Situacao == "Ativo" and Preco > 0').reset_index(drop=True)
    return lista_produtos



produtos = list_all_products(BLING_SECRET_KEY)
produtos_bling = coleta_produtos(produtos)

produtos_bling = produtos_bling.head(10)