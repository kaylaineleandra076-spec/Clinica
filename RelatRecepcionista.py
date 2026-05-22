import json
from datetime import date, datetime
from banco import ler_json

def resolver_nome_paciente(paciente_id, pacientes):
    for p in pacientes:
        if p.get('id') == paciente_id:
            return p.get('nome', 'Desconhecido')
    return 'Desconhecido'

def resolver_nome_medico(medico_id, medicos):
    for m in medicos:
        if m.get('id') == medico_id:
            return m.get('nome', 'Desconhecido')
    return 'Desconhecido'

def historico_paciente():
    print("===HISTÓRICO DO PACIENTE===")
    nome_paciente = input("Digite o nome do paciente: ").strip()
    pacientes = ler_json("pacientes.json")
    consultas = ler_json("consultas.json")
    medicos = ler_json("medicos.json")

    encontrado = False

    for paciente in pacientes:
        if paciente['nome'].lower() == nome_paciente.lower():
            encontrado = True
            print(f"\nPaciente: {paciente['nome']}")

            contador = 1

            tem_consulta = False

            for consulta in consultas:
                if consulta.get('paciente_id') == paciente['id']:
                    tem_consulta = True
                    medico_nome = resolver_nome_medico(consulta.get('medico_id'), medicos)
                    
                    if not medico_nome and consulta.get('medico_id'):
                        medico_nome = resolver_nome_medico(consulta.get('medico_id'), medicos)
                    print(f"\nConsulta {contador}:")
                    print(f" Data: {consulta.get('data')}")
                    print(f" Médico: {medico_nome}")
                    print(f" Status: {consulta.get('status')}")
                    contador += 1
            if not tem_consulta:
                print("Nenhuma consulta encontrada para este paciente.")
    if not encontrado:
        print("Paciente não encontrado.")

def relatorio_agenda_dia():
    print("===RELATÓRIO DE AGENDA DO DIA===")
    hoje = date.today()
    consultas = ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")
    medicos = ler_json("medicos.json")
    contador = 1
    for consulta in consultas:

        try:
            data_cons = datetime.fromisoformat(consulta.get('data')).date()
        except Exception:
            continue
        if data_cons == hoje:
            paciente_nome = resolver_nome_paciente(consulta.get('paciente_id'), pacientes)
            medico_nome = resolver_nome_medico(consulta.get('medico_id'), medicos)
            print(f"Consulta {contador}:")
            print(f"  Paciente: {paciente_nome}")
            print(f"  Médico: {medico_nome}")
            print(f"  Status: {consulta.get('status')}")
            contador += 1
        if contador == 1:
            print("Nenhuma consulta agendada para hoje.")

def relatorio_consulta_data():
    print("===RELATÓRIO DE CONSULTAS POR DATA===")
    data_str = input("Digite a data (AAAA-MM-DD): ").strip()
    try: 
        data_consulta = datetime.fromisoformat(data_str).date()
    except Exception:
        print("Formato de data inválido. Use AAAA-MM-DD.")
        return
    consultas = ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")
    medicos = ler_json("medicos.json")
    contador = 1

    for consulta in consultas:
        try:
            data_cons = datetime.fromisoformat(consulta.get('data')).date()
        except Exception:
            continue
        if data_cons == data_consulta:
            paciente_nome = resolver_nome_paciente(consulta.get('paciente_id'), pacientes)
            medico_nome = resolver_nome_medico(consulta.get('medico_id'), medicos)
            print(f"Consulta {contador}:")
            print(f"  Paciente: {paciente_nome}")
            print(f"  Médico: {medico_nome}")
            print(f"  Status: {consulta.get('status')}")
            contador += 1
    if contador == 1:
        print("Nenhuma consulta encontrada para esta data.")

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
    consultas= ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")
    medicos = ler_json("medicos.json")
    contador = 1

    for consulta in consultas:
        if consulta.get('status') == "Cancelada":
            try:
                data_cons = datetime.fromisoformat(consulta.get('data')).date()
            except Exception:
                continue
            if inicial <= data_cons <= final:
                paciente_nome = resolver_nome_paciente(consulta.get('paciente_id'), pacientes)
                medico_nome = resolver_nome_medico(consulta.get('medico_id'), medicos)
                print(f"Consulta {contador}:")
                print(f"  Data: {consulta.get('data')}")
                print(f"  Paciente: {paciente_nome}")
                print(f"  Médico: {medico_nome}")
                contador += 1

    if contador == 1:
        print("Nenhuma consulta cancelada encontrada.")

def pacientes_atendidos_hoje():
    print("===PACIENTES ATENDIDOS HOJE===")
    hoje = str(date.today())
    consultas = ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")
    contador = 1

    for consulta in consultas:
        if consulta.get('data') == hoje and consulta.get('status') == "Em Atendimento":
            paciente_nome = resolver_nome_paciente(consulta.get('paciente_id'), pacientes)
            print(f"Paciente {contador}: {paciente_nome}")
            contador += 1
    if contador == 1:
        print("Nenhum paciente em atendimento hoje.")