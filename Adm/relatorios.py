import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent

def relatorio_consulta_por_periodo(inicio, fim):
    consultas = ler_json("consultas.json")
    medicos = ler_json("medicos.json")
    pacientes = ler_json("pacientes.json")    
    relatorio = []
    for consulta in consultas:
        data_consulta = consulta["data"]
        if inicio <= data_consulta <= fim:
            medico = next((m for m in medicos if m["id"] == consulta["medico_id"]), None)
            paciente = next((p for p in pacientes if p["id"] == consulta["paciente_id"]), None)
            relatorio.append({
                "data": data_consulta,
                "medico": medico["nome"] if medico else "Desconecido",
                "paciente": paciente["nome"] if paciente else "Desconecido",
                "descricao": consulta.get("descricao", "")
            })