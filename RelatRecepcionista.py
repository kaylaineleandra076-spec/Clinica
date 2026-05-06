import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent
from datetime import date

# Relatorio de recepcionista e historico de pacientes

def historico_paciente():
    print("===HISTÓRICO DO PACIENTE===")
    nome_paciente = input("Digite o nome do paciente: ")
    pacientes = ler_json("pacientes.json")
    consultas = ler_json("consultas.json")

    encontrado = False
    for paciente in pacientes:
        if paciente['nome'].lower() == nome_paciente.lower():
            encontrado = True
            print(f"Paciente: {paciente['nome']}")
            contador = 1
            tem_consulta = False
            for consulta in consultas:
                if consulta["id_paciente"] == paciente["id"]:
                    tem_consulta = True
                    print(f"Consulta {contador}:")
                    print(f"  Data: {consulta['data']}")
                    print(f"  Médico: {consulta['medico']}")
                    print(f"  Status: {consulta['status']}")
                    contador += 1
            if not tem_consulta:
                print("Nenhuma consulta encontrada.")
            break
    if not encontrado:
        print("Paciente não encontrado.")

def relatorio_agenda_dia():
    print("===RELATÓRIO DE AGENDA DO DIA===")
    hoje = str(date.today())
    consultas = ler_json("consultas.json")
    contador = 1
    for consulta in consultas:
        if consulta['data'] == hoje:
            print(f"Consulta {contador}:")
            print(f"  Paciente: {consulta['paciente']}")
            print(f"  Médico: {consulta['medico']}")
            print(f"  Status: {consulta['status']}")
            contador += 1

def relatorio_consulta_data():
    print("===RELATÓRIO DE CONSULTAS POR DATA===")
    data_consulta = int(input("Digite a data (AAAA-MM-DD): "))
    consultas = ler_json("consultas.json")
    contador = 1
    for consulta in consultas:
        if consulta['data'] == data_consulta:
            print(f"Consulta {contador}:")
            print(f"  Paciente: {consulta['paciente']}")
            print(f"  Médico: {consulta['medico']}")
            print(f"  Status: {consulta['status']}")
            contador += 1

def relatorio_cancelamento():
    print("===RELATÓRIO DE CANCELAMENTOS===")
    consultas = ler_json("consultas.json")
    inicial = int(input("Digite a data inicial (AAAA-MM-DD): "))
    final = int(input("Digite a data final (AAAA-MM-DD): "))
    contador = 1
    for consulta in consultas:
        if consulta['status'].lower() == "cancelada" and inicial <= consulta['data'] <= final:
            print(f"Consulta {contador}:")
            print(f"  Paciente: {consulta['paciente']}")
            print(f"  Médico: {consulta['medico']}")
            print(f"  Data: {consulta['data']}")
            contador += 1

def pacientes_atendidos_hoje():
    print("===PACIENTES ATENDIDOS HOJE===")
    hoje = str(date.today())
    consultas = ler_json("consultas.json")
    contador = 1
    for consulta in consultas:
        if consulta['data'] == hoje and consulta['status'].lower() == "finalizada":
            print(f"Paciente {contador}: {consulta['paciente']}")
            contador += 1