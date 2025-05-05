import csv


def ler_csv(path: str) -> list[dict]:
    """Ler o arquivo CSV e carregar os dados."""
    with open(path, mode="r", encoding="utf-8") as file:
        dados = csv.DictReader(file)
        return list(dados)


def processar_dados(lista: list[dict]) -> dict:
    """Processar os dados em um dicionário, onde a chave é a categoria,
    e o valor é uma lista de dicionários, cada um contendo informações do produto
    (Produto, Quantidade, Venda)."""

    produtos_por_categoria: dict[str, list[dict]] = {}
    for produtos in lista:
        categoria = produtos["Categoria"]
        item = {
            "Produto": produtos["Produto"],
            "Quantidade": produtos["Quantidade"],
            "Venda": produtos["Venda"],
        }
        if categoria not in produtos_por_categoria:
            produtos_por_categoria[categoria] = [item]
        else:
            produtos_por_categoria[categoria].append(item)
    return produtos_por_categoria


def calcular_vendas_categoria(dicionario: dict[str, list[dict]]) -> dict:
    """Calcular o total de vendas (Quantidade * Venda) por categoria."""

    vendas_categoria = {}
    for categoria, produtos in dicionario.items():
        for produto in produtos:
            if categoria not in vendas_categoria:
                vendas_categoria[categoria] = int(produto["Quantidade"]) * float(
                    produto["Venda"]
                )
            else:
                vendas_categoria[categoria] += int(produto["Quantidade"]) * float(
                    produto["Venda"]
                )
    return vendas_categoria


path = "/Users/francomansur/Documents/jornada_de_dados/python/aula_07/desafio/dados.csv"
raw_data = ler_csv(path)
produtos_categoria = processar_dados(raw_data)
vendas_categoria = calcular_vendas_categoria(produtos_categoria)
print(vendas_categoria)
