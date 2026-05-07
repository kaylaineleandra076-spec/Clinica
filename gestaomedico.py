import json
from pathlib import Path

base = Path(__file__).parent
arquivo_medicos = base / "medicos.json"


def carregar_medicos():
    if not arquivo_medicos.exists():
        return []

    with open(arquivo_medicos, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_medicos(medicos):
    with open(arquivo_medicos, "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)


def cadastrar_medico():
    print("=== CADASTRO MÉDICO ===")

    medicos = carregar_medicos()

    nome = input("Nome Completo: ")
    crm = input("CRM: ")
    especialidade = input("Especialidade: ")

    medico_id = max([m["id"] for m in medicos], default=0) + 1

    novo_medico = {
        "id": medico_id,
        "nome": nome,
        "crm": crm,
        "especialidade": especialidade,
        "ativo": True
    }

    medicos.append(novo_medico)

    salvar_medicos(medicos)

    print("Médico cadastrado com sucesso!")


def listar_medicos():
    print("=== LISTA DE MÉDICOS ===")

    medicos = carregar_medicos()

    if not medicos:
        print("Nenhum médico cadastrado.")
        return

    for medico in medicos:
        status = "Ativo" if medico["ativo"] else "Inativo"

        print(
            f'ID: {medico["id"]} | '
            f'Nome: {medico["nome"]} | '
            f'CRM: {medico["crm"]} | '
            f'Especialidade: {medico["especialidade"]} | '
            f'Status: {status}'
        )


def editar_medico():
    print("=== EDITAR MÉDICO ===")

    medicos = carregar_medicos()

    listar_medicos()

    try:
        id_medico = int(input("ID do Médico a Editar: "))
    except ValueError:
        print("ID inválido.")
        return

    medico = next((m for m in medicos if m["id"] == id_medico), None)

    if not medico:
        print(f"Médico com ID {id_medico} não encontrado.")
        return

    nome = input(f"Novo Nome ({medico['nome']}): ")
    crm = input(f"Novo CRM ({medico['crm']}): ")
    especialidade = input(f"Nova Especialidade ({medico['especialidade']}): ")

    ativo = input("Médico ativo? (s/n): ").lower()

    if nome:
        medico["nome"] = nome

    if crm:
        medico["crm"] = crm

    if especialidade:
        medico["especialidade"] = especialidade

    if ativo == "s":
        medico["ativo"] = True

    elif ativo == "n":
        medico["ativo"] = False

    salvar_medicos(medicos)

    print("Médico atualizado com sucesso!")


def excluir_medico():
    print("=== EXCLUIR MÉDICO ===")

    medicos = carregar_medicos()

    try:
        id_medico = int(input("ID do Médico a Excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    medico = next((m for m in medicos if m["id"] == id_medico), None)

    if not medico:
        print(f"Médico com ID {id_medico} não encontrado.")
        return

    confirmar = input(
        f'Tem certeza que deseja excluir "{medico["nome"]}"? (s/n): '
    ).lower()

    if confirmar == "s":
        medicos.remove(medico)

        salvar_medicos(medicos)

        print("Médico excluído com sucesso!")

    else:
        print("Exclusão cancelada.")