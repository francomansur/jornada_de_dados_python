import glob
import os

import pandas as pd
from decorators import log_atividade


@log_atividade
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    """Extrai dados do json e cria um DataFrame."""
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivos) for arquivos in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


@log_atividade
def calcular_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula e cria a coluna 'Total Vendas."""
    df["Total Vendas"] = df["Quantidade"] * df["Venda"]
    return df


@log_atividade
def salvar_em_csv_parquet(df: pd.DataFrame, arquivo: list[str]):
    """Salva o DataFrame em csv/parquet, dependendo do argumento fornecido."""
    if "csv" in arquivo:
        df.to_csv("data/processed/dados.csv", index=False)
    if "parquet" in arquivo:
        df.to_parquet("data/processed/dados.parquet", index=False)


def pipeline_calcular_kpi_total_de_vendas_consolidado(
    pasta: str, formato_saida: list[str]
):
    """Pipelinie completa"""
    df = extrair_dados_e_consolidar(pasta)
    df_total_vendas = calcular_kpi_total_de_vendas(df)
    salvar_em_csv_parquet(df_total_vendas, formato_saida)


if __name__ == "__main__":
    pasta = "data/raw"
    formato_saida = ["csv", "parquet"]
    pipeline_calcular_kpi_total_de_vendas_consolidado(pasta, formato_saida)
