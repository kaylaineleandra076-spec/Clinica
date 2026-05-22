from datetime import date
import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent

def verificar_conflito_horario(medico_id, data, horario):
    consultas = ler_json("consultas.json")
    for consulta in consultas:
        if consulta.get("status") == "Cancelada":
            continue
        if (consulta['medico_id']) == medico_id and consulta['data'] == data and consulta['horario'] == horario:
            return True
    return False

def verificar_data_passada(data):
    hoje = date.today().isoformat()
    return data < hoje


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
    return consulta["status"] in ("Agendada", "Confirmada")
     

def validar_status_para_finalizar(consulta):
    return consulta["status"] == "em Atendimento"
    

def validar_status_para_prontuario(consulta):
    return consulta["status"] == "Em Atendimento"
        