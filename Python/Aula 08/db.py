import pandas as pd


CAMINHO_CSV = "./database.csv"


def exportar_csv(data: list[dict]):
    """
    Recebe uma lista de dicionários com a mesma estrutura e exporta para um arquivo CSV.
    """
    df = pd.DataFrame(data)
    df.to_csv(CAMINHO_CSV, index=False)
    print(f"Dados exportados com sucesso para {CAMINHO_CSV}")


def importar_csv() -> list[dict]:
    """
    Lê o arquivo CSV e retorna uma lista de dicionários.
    """
    with open(CAMINHO_CSV) as csv:
        data = csv.read()

    if not data.strip():
        return []

    df = pd.read_csv(CAMINHO_CSV)
    return df.to_dict(orient='records')
