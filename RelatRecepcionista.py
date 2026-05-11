import json
from pathlib import Path
from banco import ler_json
base = Path(__file__).parent
from datetime import date
from datetime import datetime

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
                # nos JSONs as consultas têm chaves paciente_id e medico_id
                if consulta.get("paciente_id") == paciente.get("id") or consulta.get("paciente_id") == paciente.get("id"):
                    tem_consulta = True
                    medico_nome = consulta.get('medico')
                    # se só há medico_id no registro, tentamos resolver o nome
                    if not medico_nome and consulta.get('medico_id'):
                        medicos = ler_json('medicos.json')
                        for m in medicos:
                            if m.get('id') == consulta.get('medico_id'):
                                medico_nome = m.get('nome')
                                break
                    print(f"Consulta {contador}:")
                    print(f"  Data: {consulta.get('data')}")
                    print(f"  Médico: {medico_nome}")
                    print(f"  Status: {consulta.get('status')}")
                    contador += 1
            if not tem_consulta:
                print("Nenhuma consulta encontrada.")
            break
    if not encontrado:
        print("Paciente não encontrado.")

def relatorio_agenda_dia():
    print("===RELATÓRIO DE AGENDA DO DIA===")
    hoje = date.today()
    consultas = ler_json("consultas.json")
    contador = 1
    for consulta in consultas:
        # converte a data da consulta para date para comparação segura
        try:
            data_cons = datetime.fromisoformat(consulta.get('data')).date()
        except Exception:
            continue
        if data_cons == hoje:
            paciente_nome = consulta.get('paciente')
            if not paciente_nome and consulta.get('paciente_id'):
                pacientes = ler_json('pacientes.json')
                for p in pacientes:
                    if p.get('id') == consulta.get('paciente_id'):
                        paciente_nome = p.get('nome')
                        break
            medico_nome = consulta.get('medico')
            if not medico_nome and consulta.get('medico_id'):
                medicos = ler_json('medicos.json')
                for m in medicos:
                    if m.get('id') == consulta.get('medico_id'):
                        medico_nome = m.get('nome')
                        break
            print(f"Consulta {contador}:")
            print(f"  Paciente: {paciente_nome}")
            print(f"  Médico: {medico_nome}")
            print(f"  Status: {consulta.get('status')}")
            contador += 1

def relatorio_consulta_data():
    print("===RELATÓRIO DE CONSULTAS POR DATA===")
    data_str = input("Digite a data (AAAA-MM-DD): ")
    try:
        data_consulta = datetime.fromisoformat(data_str).date()
    except Exception:
        print("Formato de data inválido. Use AAAA-MM-DD.")
        return
    consultas = ler_json("consultas.json")
    contador = 1
    for consulta in consultas:
        try:
            data_cons = datetime.fromisoformat(consulta.get('data')).date()
        except Exception:
            continue
        if data_cons == data_consulta:
            paciente_nome = consulta.get('paciente')
            if not paciente_nome and consulta.get('paciente_id'):
                pacientes = ler_json('pacientes.json')
                for p in pacientes:
                    if p.get('id') == consulta.get('paciente_id'):
                        paciente_nome = p.get('nome')
                        break
            medico_nome = consulta.get('medico')
            if not medico_nome and consulta.get('medico_id'):
                medicos = ler_json('medicos.json')
                for m in medicos:
                    if m.get('id') == consulta.get('medico_id'):
                        medico_nome = m.get('nome')
                        break
            print(f"Consulta {contador}:")
            print(f"  Paciente: {paciente_nome}")
            print(f"  Médico: {medico_nome}")
            print(f"  Status: {consulta.get('status')}")
            contador += 1

def relatorio_cancelamento():
    print("===RELATÓRIO DE CANCELAMENTOS===")
    consultas = ler_json("consultas.json")
    inicial_str = input("Digite a data inicial (AAAA-MM-DD): ")
    final_str = input("Digite a data final (AAAA-MM-DD): ")
    try:
        inicial = datetime.fromisoformat(inicial_str).date()
        final = datetime.fromisoformat(final_str).date()
    except Exception:
        print("Formato de data inválido. Use AAAA-MM-DD.")
        return
    contador = 1
    for consulta in consultas:
        if consulta.get('status', '').lower() == "cancelada":
            try:
                data_cons = datetime.fromisoformat(consulta.get('data')).date()
            except Exception:
                continue
            if inicial <= data_cons <= final:
                paciente_nome = consulta.get('paciente')
                if not paciente_nome and consulta.get('paciente_id'):
                    pacientes = ler_json('pacientes.json')
                    for p in pacientes:
                        if p.get('id') == consulta.get('paciente_id'):
                            paciente_nome = p.get('nome')
                            break
                medico_nome = consulta.get('medico')
                if not medico_nome and consulta.get('medico_id'):
                    medicos = ler_json('medicos.json')
                    for m in medicos:
                        if m.get('id') == consulta.get('medico_id'):
                            medico_nome = m.get('nome')
                            break
                print(f"Consulta {contador}:")
                print(f"  Paciente: {paciente_nome}")
                print(f"  Médico: {medico_nome}")
                print(f"  Data: {consulta.get('data')}")
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