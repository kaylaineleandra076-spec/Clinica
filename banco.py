import json
from pathlib import Path

base = Path(__file__).parent


def ler_json(arquivo):
    caminho = base / 'jsons' / arquivo
    try:
        with open(caminho, 'r', enconding= 'utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado. Criando um novo arquivo vazio.")
        return []
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo '{arquivo}'. Verifique se o conteúdo é um JSON válido.")
        return []
    
def salvar_json(arquivo, dados):
    caminho = base / 'jsons' / arquivo
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def gerar_id(arquivo):
    dados = ler_json(arquivo)
    if not dados:
        return "001"
    maior = max(int(item.get('id', '0')) for item in dados)
    return str(maior + 1).zfill(3)