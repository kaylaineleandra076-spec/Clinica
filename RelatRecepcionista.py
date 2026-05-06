import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent

def historico_paciente():
    pacientes = ler_json("pacientes.json")
    consultas = ler_json("consultas.json")
    for paciente in pacientes:
        print(f"Paciente: {paciente['nome']}")
        for i, consulta in enumerate(consultas):
            if consulta["id_paciente"] == paciente["id"]:
                print(f"Consulta {i + 1}:")
                print(f"Data: {consulta['data']}")
                print(f"Médico: {consulta['medico']}")
                print(f"Status: {consulta['status']}")