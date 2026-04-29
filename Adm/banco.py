import json
from pathlib import Path
base = Path(__file__).parent

def ler_json(arquivo):
    try:

        with open( arquivo, "r", encoding= "utf-8") as f:
            return json.load(f)
    except FileExistsError:
        return[]

def salvar_json(arquivo , dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def gerar_id(lista):
    if not lista:
        return 1
    else:
        return max(item["id"] for item in lista) + 1
