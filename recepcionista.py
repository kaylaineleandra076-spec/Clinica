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
    salvar_json('pacientes.json', pacientes)
    print("Paciente cadastrado com sucesso!")

def editar_paciente():
    pacientes= ler_json('pacientes.json')

    id_paciente= int(input("Digite o ID do paciente que deseja editar: "))

    for paciente in pacientes:

        if paciente['id']== id_paciente:
            print(f"Paciente encontrado: {paciente['nome']}")
            nome= input("Digite o novo nome do paciente (deixe em branco o nome atual): ")
            idade= input("Digite a nova idade do paciente (deixe em branco a idade atual)")
            contato= input("Digite o novo contato do paciente (deixe em branco o contato atual): ")
            CPF= input("Digite o novo CPF do paciente (deixe em branco o CPF atual): ")

            if nome:
                paciente['nome']= nome
            if idade:
                paciente['idade']= idade
            if contato:
                paciente['contato']= contato
            if CPF:
                paciente['CPF']= CPF
            salvar_json('pacientes.json', pacientes)
            print("Paciente editado com sucesso!")
            return
    print("Paciente não encontrado!")

def buscar_paciente():
    pacientes= ler_json('pacientes.json')

    id_paciente= int(input("Digite o ID do paciente que deseja buscar: "))

    for paciente in pacientes:
        if paciente['id']== id_paciente:
            print(f"Paciente encontrado: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"Contato: {paciente['contato']}")
            print(f"CPF: {paciente['CPF']}")
            return
    print("Paciente não encontrado!")

def listar_pacientes():
    pacientes= ler_json('pacientes.json')

    if not pacientes:
        print("Nenhum paciente encontrado!")
        return
    print("=== Lista de Pacientes ===")
    for paciente in pacientes:
        print(f"Id: {paciente['id']}")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"Contato: {paciente['contato']}")
        print(f"CPF: {paciente['CPF']}")
        print("==========================")


#Gestao de consultas:

def gerar_id(lista):
    if not lista:
        return 1
    else:
        return max(item['id'] for item in lista) + 1

def marcar_consulta():
    pacientes = ler_json('pacientes.json')
    medicos = ler_json('medicos.json')
    consultas = ler_json('consultas.json')

    if not pacientes:
        print("Nenhum paciente encontrado! Cadastre um paciente antes de marcar uma consulta.")
        return
    if not medicos:
        print("Nenhum médico encontrado! Cadastre um médico antes de marcar uma consulta.")
        return
    
    print("=== Marcar Consulta ===")
    id_paciente = int(input("Digite o ID do paciente: "))
    paciente = next((p for p in pacientes if p['id'] == id_paciente), None)
    
    if not paciente:
        print("Paciente não encontrado!")
        return
    print("Pacientes encontrados:")
    for medico in medicos:
        print(f"Id: {medico['id']} - Nome: {medico['nome']} - Especialidade: {medico['especialidade']}")
    id_medico = int(input("Digite o ID do médico: "))
    medico = next((m for m in medicos if m['id'] == id_medico), None)

    if not medico:
        print("Médico não encontrado!")
        return
    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    hora = input("Digite a hora da consulta (HH:MM): ")

    consulta = {
        "id": gerar_id(consultas),
        "id_paciente": paciente['id'],
        "id_medico": medico['id'],
        "data": data,
        "hora": hora,
        "status": "Agendada"
    }
    consultas.append(consulta)
    salvar_json('consultas.json', consultas)
    print("Consulta marcada com sucesso!")

