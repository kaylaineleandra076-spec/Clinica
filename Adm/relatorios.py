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
    medicos_ativos = [m for m in medicos if m["ativo"]]
    
    print(f"Total de médicos ativos: {len(medicos_ativos)}")

def relatorio_consultas_por_medico():
    consultas = ler_json("consultas.json")
    medicos = ler_json("medicos.json")
    
    relatorio = {}
    for medico in medicos:
        relatorio[medico["id"]] = {
            "nome": medico["nome"],
            "total_consultas": 0
        }
    
    for consulta in consultas:
        medico_id = consulta["medico_id"]
        if medico_id in relatorio:
            relatorio[medico_id]["total_consultas"] += 1
    
    return relatorio

def relatorio_atendimentos_do_dia():
    consultas = ler_json("consultas.json")
    relatorio = []
    for consulta in consultas:
        if consulta["data"] == "2026-06-05":
            relatorio.append(consulta)
    return relatorio

def relatorio_pacientes_mais_atendidos():
    consultas = ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")
    
    relatorio = {}
    for paciente in pacientes:
        relatorio[paciente["id"]] = {
            "nome": paciente["nome"],
            "total_atendimentos": 0
        }
    
    for consulta in consultas:
        paciente_id = consulta["paciente_id"]
        if paciente_id in relatorio:
            relatorio[paciente_id]["total_atendimentos"] += 1
    
    return relatorio