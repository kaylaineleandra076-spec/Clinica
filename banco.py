import json
from pathlib import Path

base = Path(__file__).parent


def ler_json(arquivo):
    """Tenta carregar um JSON a partir de caminhos comuns do projeto.

    Procura na ordem:
      1) caminho informado (relativo/absoluto)
      2) relativo ao diretório do módulo
      3) dentro da pasta 'jsons' do projeto

    Retorna uma lista vazia se o arquivo não existir ou estiver inválido.
    """
    candidates = [Path(arquivo)]
    p = Path(arquivo)
    if not p.is_absolute():
        candidates.append(base / arquivo)
        candidates.append(base / 'jsons' / arquivo)

    for c in candidates:
        try:
            with open(c, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            continue
        except json.JSONDecodeError:
            # Arquivo existe mas está com JSON inválido
            return []
    return []


def salvar_json(arquivo, dados):
    """Salva dados em JSON; por padrão grava em ./jsons/ quando caminho relativo."""
    p = Path(arquivo)
    if not p.is_absolute():
        p = base / 'jsons' / arquivo
        p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def gerar_id(lista):
    if not lista:
        return 1
    # tenta extrair inteiros mesmo que IDs venham como strings
    try:
        return max(int(item.get("id", 0)) for item in lista) + 1
    except Exception:
        # fallback: usar comprimento + 1
        return len(lista) + 1
