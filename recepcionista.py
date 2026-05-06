import json
from pathlib import Path
base = Path(__file__).parent
from banco import ler_json , salvar_json

def cadastrar_paciente():
    pacientes= ler_json('pacientes.json')

    nome= input("Digite o nome do paciente: ")
    idade= input("Digite a idade do paciente: ")
    contato= input("Digite o contato do pacciente: ")
    CPF= input("Digite o CPF do paciente: ")

    paciente= {
        "id": gerar_id(pacientes),
        "nome": nome,
        "idade": idade,
        "contato": contato,
        "CPF": CPF
    }

    paciente.append(paciente)