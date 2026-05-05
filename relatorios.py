import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent

def relatorio_consulta_por_periodo(data_inicial, data_final):
    consultas = ler_json("consultas.json")
    relatorio = []
    for consulta in consultas:
        if data_inicial <= consulta["data"] <= data_final:
            relatorio.append(consulta)
    return relatorio