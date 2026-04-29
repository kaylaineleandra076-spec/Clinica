import json
from pathlib import Path

base = Path(__file__).parent
arquivo_medicos = base / "medicos.json"

def cadastrar_medico():
    print("===CADASTRO MEDICO===")
    nome= input("Nome Completo:")
    CRM= input("CRM:")
    especialidade= input("Especialidades:")

    with open ("medicos.json" , "r", encoding="utf-8") as f:
        medicos = json.load(f)
        medico_id = max([m["id"] for m in medicos], default=0) + 1
        novo_medico = {
            "id": medico_id,
            "nome": nome,
            "CRM": CRM,
            "especialidade": especialidade
        }
        medicos.append(novo_medico)

    with open("medicos.json", "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)   

def editar_medico():
    print("===EDITAR MEDICO===")

    id = int(input("ID do Médico a Editar:"))
    
    with open("medicos.json", "r", encoding="utf-8") as f:
        medicos = json.load(f)
        medico = next((m for m in medicos if m["id"] == id), None)
        if not medico:
            print(f"Médico com ID {id} não encontrado.")
        
            return
        
        print(f"Editando Médico: {medico['nome']} (ID: {medico['id']})")
    
        nome = input(f"Novo Nome (deixe em branco para manter '{medico['nome']}'): ")
        CRM = input(f"Novo CRM (deixe em branco para manter '{medico['CRM']}'): ")
        especialidade = input(f"Nova Especialidade (deixe em branco para manter '{medico['especialidade']}'): ")
        
        if nome:
            medico["nome"] = nome
        if CRM:
            medico["CRM"] = CRM
        if especialidade:
            medico["especialidade"] = especialidade

    with open("medicos.json", "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)


def excluir_medico():
    print("===EXCLUIR MEDICO===")

    id = int(input("ID do Médico a Excluir:"))
    
    with open("medicos.json", "r", encoding="utf-8") as f:
        medicos = json.load(f)
        medico = next((m for m in medicos if m["id"] == id), None)
        if not medico:
            print(f"Médico com ID {id} não encontrado.")
            return
        
        medicos.remove(medico)
        print(f"Médico '{medico['nome']}' (ID: {medico['id']}) excluído com sucesso.")

    with open("medicos.json", "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)