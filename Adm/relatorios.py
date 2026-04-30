import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent

def relatorio_consulta_por_periodo(data_inicio, data_fim):
    consultas = ler_json("consultas.json")
    relatorio = []
    for consulta in consultas:
        if data_inicio <= consulta["data"] <= data_fim:
            relatorio.append(consulta)
    return relatorio

def relatorio_consultas_canceladas():
    consultas = ler_json("consultas.json")
    relatorio = []
    for consulta in consultas:
        if consulta["status"] == "cancelada":
            relatorio.append(consulta)
    return relatorio

def relatorio_pacientes_cadastados():
    pacientes = ler_json("pacientes.json")
    for i, paciente in enumerate(pacientes):
        print(f"Temos {i + 1} pacientes cadastrados.")

def relatorio_medicos_ativos():
    medicos = ler_json("medicos.json")
    for i, medico in enumerate(medicos):
        print(f"Temos {i + 1} médicos ativos.")