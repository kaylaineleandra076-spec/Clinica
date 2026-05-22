import json
from pathlib import Path
base = Path(__file__).parent
from banco import ler_json , salvar_json
from datetime import date

def listar_consultas_do_dia():
    raise NotImplementedError

def painel_recepcionista(usuario):
    from RelatRecepcionista import (
        historico_paciente,
        relatorio_agenda_dia,
        relatorio_consulta_data,
        relatorio_cancelamento,
        pacientes_atendidos_hoje,
    )

    while True:
        print('\n=== PAINEL RECEPCIONISTA ===')
        print('1 - Cadastrar paciente')
        print('2 - Editar paciente')
        print('3 - Buscar paciente')
        print('4 - Listar pacientes')
        print('5 - Marcar consulta')
        print('6 - Reagendar consulta')
        print('7 - Cancelar consulta')
        print('8 - Confirmar presença')
        print('9 - Consultas do dia')
        print('10 - Histórico do paciente')
        print('11 - Relatório: agenda do dia')
        print('12 - Relatório: consultas por data')
        print('13 - Relatório: cancelamentos')
        print('14 - Pacientes atendidos hoje')
        print('0 - Sair')

        opc = input('Escolha uma opção: ')
        if opc == '1':
            cadastrar_paciente()
        elif opc == '2':
            editar_paciente()
        elif opc == '3':
            buscar_paciente()
        elif opc == '4':
            listar_pacientes()
        elif opc == '5':
            marcar_consulta()
        elif opc == '6':
            reagendar_consulta()
        elif opc == '7':
            cancelar_consulta()
        elif opc == '8':
            confirmar_presença()
        elif opc == '9':
            listar_consultas_do_dia()
        elif opc == '10':
            historico_paciente()
        elif opc == '11':
            relatorio_agenda_dia()
        elif opc == '12':
            relatorio_consulta_data()
        elif opc == '13':
            relatorio_cancelamento()
        elif opc == '14':
            pacientes_atendidos_hoje()
        elif opc == '0':
            break
        else:
            print('Opção inválida.')

def cadastrar_paciente():
    pacientes= ler_json('pacientes.json')

    nome= input("Digite o nome do paciente: ")
    idade= input("Digite a idade do paciente: ")
    contato= input("Digite o contato do pacciente: ")
    CPF= input("Digite o CPF do paciente: ")

    paciente= {
        "id": gerar_id(pacientes),
        "nome": nome,
        "idade": idade,
        "contato": contato,
        "CPF": CPF
    }

    pacientes.append(paciente)
    salvar_json('pacientes.json', pacientes)
    print("Paciente cadastrado com sucesso!")

def editar_paciente():
    pacientes= ler_json('pacientes.json')

    id_paciente= int(input("Digite o ID do paciente que deseja editar: "))

    for paciente in pacientes:

        if paciente['id']== id_paciente:
            print(f"Paciente encontrado: {paciente['nome']}")
            nome= input("Digite o novo nome do paciente (deixe em branco o nome atual): ")
            idade= input("Digite a nova idade do paciente (deixe em branco a idade atual)")
            contato= input("Digite o novo contato do paciente (deixe em branco o contato atual): ")
            CPF= input("Digite o novo CPF do paciente (deixe em branco o CPF atual): ")

            if nome:
                paciente['nome']= nome
            if idade:
                paciente['idade']= idade
            if contato:
                paciente['contato']= contato
            if CPF:
                paciente['CPF']= CPF
            salvar_json('pacientes.json', pacientes)
            print("Paciente editado com sucesso!")
            return
    print("Paciente não encontrado!")

def buscar_paciente():
    pacientes= ler_json('pacientes.json')

    id_paciente= int(input("Digite o ID do paciente que deseja buscar: "))

    for paciente in pacientes:
        if paciente['id']== id_paciente:
            print(f"Paciente encontrado: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"Contato: {paciente['contato']}")
            print(f"CPF: {paciente['CPF']}")
            return
    print("Paciente não encontrado!")

def listar_pacientes():
    pacientes= ler_json('pacientes.json')

    if not pacientes:
        print("Nenhum paciente encontrado!")
        return
    print("=== Lista de Pacientes ===")
    for paciente in pacientes:
        print(f"Id: {paciente['id']}")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"Contato: {paciente['contato']}")
        print(f"CPF: {paciente['CPF']}")
        print("==========================")

#Gestao de consultas:

def gerar_id(lista):
    if not lista:
        return 1
    else:
        return max(item['id'] for item in lista) + 1

def marcar_consulta():
    pacientes = ler_json('pacientes.json')
    medicos = ler_json('medicos.json')
    consultas = ler_json('consultas.json')

    if not pacientes:
        print("Nenhum paciente encontrado! Cadastre um paciente antes de marcar uma consulta.")
        return
    if not medicos:
        print("Nenhum médico encontrado! Cadastre um médico antes de marcar uma consulta.")
        return
    
    print("=== Marcar Consulta ===")
    id_paciente = int(input("Digite o ID do paciente: "))
    paciente = next((p for p in pacientes if p['id'] == id_paciente), None)
    
    if not paciente:
        print("Paciente não encontrado!")
        return
    print("Pacientes encontrados:")
    for medico in medicos:
        print(f"Id: {medico['id']} - Nome: {medico['nome']} - Especialidade: {medico['especialidade']}")
    id_medico = int(input("Digite o ID do médico: "))
    medico = next((m for m in medicos if m['id'] == id_medico), None)

    if not medico:
        print("Médico não encontrado!")
        return
    # usar formato ISO para data (AAAA-MM-DD) para compatibilidade com relatórios
    data = input("Digite a data da consulta (AAAA-MM-DD): ")
    horario = input("Digite a hora da consulta (HH:MM): ")

    consulta = {
        "id": gerar_id(consultas),
        "paciente_id": paciente['id'],
        "medico_id": medico['id'],
        "data": data,
        "horario": horario,
        "status": "Agendada"
    }
    consultas.append(consulta)
    salvar_json('consultas.json', consultas)
    print("Consulta marcada com sucesso!")

def reagendar_consulta():
    consultas = ler_json('consultas.json')

    if not consultas:
        print("Nenhuma consulta encontrada!")
        return
    
    print("=== Reagendar Consulta ===")
    id_consulta = int(input("Digite o ID da consulta que deseja reagendar: "))
    consulta = next((c for c in consultas if c['id'] == id_consulta), None)

    if not consulta:
        print("Consulta não econtrada!")
        return
    
    nova_data = input("Digite a nova data da consulta (AAAA-MM-DD): ")
    nova_hora = input("Digite a nova hora da consulta (HH:MM): ")
    consulta['data'] = nova_data
    consulta['horario'] = nova_hora
    salvar_json('consultas.json', consultas)

    print("Consulta reagendada com sucesso!")

def cancelar_consulta():
    consultas = ler_json('consultas.json')

    if not consultas:
        print("Nenhuma consulta encontrada!")
        return
    
    print("=== Cancelar Consulta ===")
    id_consulta = int(input("Digite o ID da consulta que deseja cancelar: "))
    consulta = next((c for c in consultas if c['id'] == id_consulta), None)

    if not consulta:
        print("Consulta não econtrada!")
        return
    
    consulta['status']= "Cancelada"
    salvar_json('consultas.json', consultas)

    print("Consulta cancelada com sucesso!")

def confirmar_presenca():
    consultas = ler_json('consultas.json')
    pacientes = ler_json('pacientes.json')
    hoje = str(date.today())

    consultas_hoje = [c for c in consultas if c.get('data') == hoje and c.get('status') == 'Agendada']

    if not consultas_hoje:
        print("Nenhuma consulta encontrada para hoje")
        return

    for c in consultas_hoje:
        p = next((p for p in pacientes if p.get('id') == c.get('paciente_id')), None)
        nome_p = p.get('nome') if p else 'Paciente Desconhecido'
        print(f"ID: {c['id']} | {nome_p} | {c.get('horario')}")

    consulta_id = input("\nID da consulta para confirmar: ").strip()
    consulta_sel = next((c for c in consultas_hoje if str(c.get('id')) == consulta_id), None)
    if not consulta_sel:
        print("Consulta não encontrada.")
        return False
    consulta_sel['status'] = 'Confirmada'
    salvar_json('consultas.json', consultas)
    print("Presença confirmada com sucesso!")
    return True
    
def consultas_do_dia():
    print("=== CONSULTAS DO DIA ===")

    consultas = ler_json('consultas.json')
    pacientes = ler_json('pacientes.json')
    medicos = ler_json('medicos.json')
    hoje = str(date.today())

    consulta_hoje = [c for c in consultas if c.get('data') == hoje]

    if not consulta_hoje:
        print("Nenhuma consulta para hoje")
        return
    
    for c in sorted(consulta_hoje, key=lambda x: x.get('horario', '')):

        paciente = next((p for p in pacientes if p.get('id') == c.get('paciente_id')), None)
        medico = next((m for m in medicos if m.get('id') == c.get('medico_id')), None)
        nome_p = paciente.get('nome') if paciente else 'Paciente Desconhecido'
        nome_m = medico.get('nome') if medico else 'Médico Desconhecido'
        print(f"{c.get('horario')} | {nome_p} | Dr(a). {nome_m} | {c.get('status')}")

def menu_relatorios():
    print("=== RELATÓRIOS ===")
    print("1 - Histórico do paciente")
    print("2 - Agenda do dia")
    print("3 - Consultas por data")
    print("4 - Cancelamentos")
    print("0 - Voltar")

    op = input("\nEscolha uma opção: ").strip()

    if op == '1':
        from RelatRecepcionista import historico_paciente
        historico_paciente()
    elif op == '2':
        from RelatRecepcionista import relatorio_agenda_dia
        relatorio_agenda_dia()
    elif op == '3':
        from RelatRecepcionista import relatorio_consulta_data
        relatorio_consulta_data()
    elif op == '4':
        from RelatRecepcionista import relatorio_cancelamento
        relatorio_cancelamento()
    elif op == '0':
        return
    else:
        print("Opção inválida. Tente novamente.")

#prontuarios