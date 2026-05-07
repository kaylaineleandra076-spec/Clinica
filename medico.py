import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent
from datetime import date
import regras
#Agendas medico

def ver_agenda_hoje():
    print("===AGENDA DO DIA===")
    hoje = str(date.today())
    consultas = ler_json("consultas.json")
    medico_id = int(input("Digite o ID do médico: "))
    contador = 1
    for consulta in consultas:
        if consulta['data'] == hoje and consulta['id_medico'] == medico_id:
            print(f"Consulta {contador}:")
            print(f"Horário: {consulta['horario']}")
            print(f"  Paciente: {consulta['paciente']}")
            print(f"  Status: {consulta['status']}")
            contador += 1

def ver_agenda_futura():
    print("===AGENDA FUTURA===")
    hoje = str(date.today())
    consultas = ler_json("consultas.json")
    medico_id = int(input("Digite o ID do médico: "))
    contador = 1
    for consulta in consultas:
        if consulta['data'] > hoje and consulta['id_medico'] == medico_id:
            print(f"Consulta {contador}:")
            print(f"Data: {consulta['data']}")
            print(f"Horário: {consulta['horario']}")
            print(f"  Paciente: {consulta['paciente']}")
            print(f"  Status: {consulta['status']}")
            contador += 1

#Atendimento

def iniciar_atendimento(medico_id, consulta_id):
    print("===== ATENDIMENTO ======")
    consultas = ler_json("consultas.json")
    medicos   = ler_json("medicos.json")
    if medico_id not in [medico['id'] for medico in medicos]:
        print("Médico não encontrado.")
        return
    consulta = next((c for c in consultas if c['id'] == consulta_id and c['id_medico'] == medico_id), None)
    if not consulta:
        print("Consulta não encontrada.")
        return
    if consulta['status'] == 'agendada':
        consulta['status'] = 'em atendimento'
        with open(base / "consultas.json", "w") as f:
            json.dump(consultas, f, indent=4)
    else:
        print(f"Consulta não pode ser iniciada. Status atual: '{consulta['status']}'.")

def finalizar_atendimento(medico_id, consulta_id):
    print("===== FINALIZAR ATENDIMENTO ======")
    consultas = ler_json("consultas.json")
    medicos   = ler_json("medicos.json")
    if medico_id not in [medico['id'] for medico in medicos]:
        print("Médico não encontrado.")
        return
    consulta = next((c for c in consultas if c['id'] == consulta_id and c['id_medico'] == medico_id), None)
    if not consulta:
        print("Consulta não encontrada.")
        return
    if consulta['status'] == 'em atendimento':
        consulta['status'] = 'finalizada'
        with open(base / "consultas.json", "w") as f:
            json.dump(consultas, f, indent=4)
    else:
        print(f"Consulta não pode ser finalizada. Status atual: '{consulta['status']}'.")

