import json
from datetime import date
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent

def verificar_conflito_horario(medico_id, data, horario):
    consultas = ler_json("consultas.json")
    for consulta in consultas:
        if consulta["medico_id"] == medico_id and consulta["data"] == data and consulta["horario"] == horario:
            return True
    return False

def verificar_data_passada(data):


def medico_existe(medico_id):
    medicos = ler_json("medicos.json")
    for medico in medicos:
        if medico["id"] == medico_id:
            return True
    return False

def paciente_existe(paciente_id):
    pacientes = ler_json("pacientes.json")
    for paciente in pacientes:
        if paciente["id"] == paciente_id:
            return True
    return False

def validar_status_para_iniciar(consulta):
    if consulta["status"] == "agendada":
        return True
    return False

def validar_status_para_finalizar(consulta):
    if consulta["status"] == "em andamento":
        return True
    return False

def validar_status_para_prontuario(consulta):
    if consulta["status"] == "finalizada":
        return True
    return False