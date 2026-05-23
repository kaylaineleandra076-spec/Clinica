from datetime import date
import json
from banco import ler_json, salvar_json
from regras import validar_status_para_iniciar, validar_status_para_finalizar, validar_status_para_prontuario

def resolver_nome_paciente(paciente_id, pacientes):
    for p in pacientes:
        if p.get('id') == paciente_id:
            return p.get('nome', 'Desconecido')
    return 'Desconecido'

def painel_medico(usuario):
    print("===== PAINEL MÉDICO =====")
    print(f"Bem-vindo, Dr(a). {usuario['nome'].upper()}!")
    print("====================================")
    hoje= str(date.today())
    consultas = ler_json('consultas.json')
    medico_id = usuario['id']

    hoje_list= [c for c in consultas if c.get('data')== hoje and c.get('medico_id') == medico_id]
    finalizadas= [c for c in hoje_list if c.get('status') == 'Finalizada']
    pendentes = [c for c in hoje_list if c.get('status') in ('Agendada', 'Confirmada')] 
    proxima= sorted(hoje_list, key=lambda c: c.get('horario', ''))
    proxima_horario= proxima[0]['horario'] if proxima else '--'

    print(f" Minhas Consultas hoje: {len(hoje_list)}")
    print(f" Próxima Consulta: {proxima_horario}")
    print(f" Conultas Finalizadas hoje: {len(finalizadas)}")
    print(f" Pacientes aguardando: {len(pendentes)}")
    print(f"=============================================\n")

def ver_agenda_hoje(medico_id):
    print("=== AGENDA DO DIA ===")
    hoje = str(date.today())
    consultas = ler_json("consultas.json")
    contador = 1

    for consulta in consultas:
        if consulta.get('data') == hoje and consulta.get('medico_id') == medico_id:
            paciente_nome= resolver_nome_paciente(consulta.get('paciente_id'))
            print(f"Consulta {contador}:")
            print(f"Horário: {consulta.get('horario')}")
            print(f"  Paciente: {paciente_nome}")
            print(f"  Status: {consulta['status']}")
            contador += 1
        if contador == 1:
            print("Nenhuma consulta para hoje.")

def ver_agenda_futura(medico_id):
    print("===AGENDA FUTURA===")
    hoje = str(date.today())
    consultas = ler_json("consultas.json")
    contador = 1

    for consulta in sorted(consultas, key=lambda c: (c.get('data', ''), c.get('horario', ''))):
        if consulta.get('data', '') > hoje and consulta.get('medico_id') == medico_id:
            paciente_nome= resolver_nome_paciente(consulta.get('paciente_id'))
            print(f"Consulta: {contador}")
            print(f"Data: {consulta.get('data')}")
            print(f"Horário: {consulta.get('horario')}")
            print(f"Paciente: {paciente_nome}")
            print(f"Status: {consulta.get('status')}")
            contador += 1
            
    if contador == 1:
        print("Nenhuma consulta futura.")

#Atendimento

def iniciar_atendimento(medico_id, consulta_id):
    print("===== INICIAR ATENDIMENTO ======")
    consulta_id = input("Digite o ID da consulta: ").strip()
    consultas= ler_json("consultas.json")

    consulta = next((c for c in consultas if c.get('id') == consulta_id and c.get('medico_id') == medico_id), None)
    if not consulta:
        print("Consulta não encontrada ou não pertence a você.")
        return
    if validar_status_para_iniciar(consulta):
        consulta['status']= 'Em Atendimento'
        salvar_json('consultas.json', consultas)
        print("Atendimento iniciado com sucesso!")
    else:
        print(f"Não é possível iniciar. Status atual: '{consulta['status']}'.")

def finalizar_atendimento(medico_id, consulta_id):
    print("===== FINALIZAR ATENDIMENTO ======")
    consulta_id = input("Digite o ID da consulta: ").strip()
    consultas = ler_json("consultas.json")

    consulta = next((c for c in consultas if c.get('id') == consulta_id and c.get('medico_id') == medico_id), None)
    if not consulta:
        print("Consulta não encontrada ou não pertence a você.")
        return
    
    if validar_status_para_finalizar(consulta):
        consulta['status'] = 'finalizada'
        salvar_json('consultas.json', consultas)
        print("Atendimento finalizado com sucesso!")
    else:
        print(f"Não é possível finalizar. Status atual: '{consulta['status']}'.")

#prontuarios

def registrar_prontuario(medico_id, consulta_id):
    print("===== REGISTRAR PRONTUARIO ======")
    consulta_id = input("Digite o ID da consulta: ").strip()
    consultas = ler_json("consultas.json")

    consulta = next((c for c in consultas if c.get('id') == consulta_id and c.get('medico_id') == medico_id), None)
    if not consulta:
        print("Consulta não encontrada ou não pertence a você.")
        return

    if not validar_status_para_prontuario(consulta): 
        print(f"Não é possível registrar prontuário. Status atual: '{consulta['status']}'.")
        return

    prontuarios = ler_json("prontuarios.json")
    from banco import gerar_id

    paciente_nome = resolver_nome_paciente(consulta.get('paciente_id'))
    medicos = ler_json("medicos.json")
    medico_nome = next((m['nome'] for m in medicos if m['id'] == medico_id), 'Desconhecido')

    diagnostico = input("Diagnóstico: ").strip()
    receita = input("Receita médica: ").strip()
    observacoes = input("Observações: ").strip()

    prontuario = {
        "id": gerar_id(prontuarios),
        "consulta_id": consulta_id,
        "paciente_nome": paciente_nome,
        "medico_nome": medico_nome,
        "data": consulta.get('data'),
        "diagnostico": diagnostico,
        "receita": receita,
        "observacoes": observacoes
    }

    prontuarios.append(prontuario)
    salvar_json("prontuarios.json", prontuarios)
    print("Prontuário registrado com sucesso!")

def ver_prontuarios_paciente(medico_id, consulta_id):
    print("===== VER PRONTUÁRIO DO PACIENTE ======")

    nome = input("Digite o nome do paciente: ").strip()
    prontuarios = ler_json("prontuarios.json")
    encontrou = False

    for p in prontuarios:
        if p.get('paciente_nome', '').lower() == nome.lower():
            encontrou = True
            print(f"Data: {p.get('data')} | Médico: {p.get('medico_nome')}")
            print(f"  Diagnóstico: {p.get('diagnostico')}")
            print(f"  Receita: {p.get('receita')}")
            print(f"  Observações: {p.get('observacoes')}")

    if not encontrou:
        print("Nenhum prontuário encontrado para este paciente.")


def buscar_historico_paciente(medico_id, consulta_id):
    print("===== HISTÓRICO DO PACIENTE ======")

    nome = input("Digite o nome do paciente: ").strip()
    pacientes = ler_json("pacientes.json")
    consultas = ler_json("consultas.json")

    paciente = next((p for p in pacientes if p.get('nome', '').lower() == nome.lower()), None)
    if not paciente:
        print("Paciente não encontrado.")
        return

    encontrou = False
    for consulta in consultas:
        if consulta.get('paciente_id') == paciente.get('id'):
            encontrou = True
            medicos = ler_json("medicos.json")
            medico_nome = next((m['nome'] for m in medicos if m['id'] == consulta.get('medico_id')), 'Desconhecido')
            print(f"Data: {consulta.get('data')} | Médico: {medico_nome} | Status: {consulta.get('status')}")

    if not encontrou:
        print("Nenhuma consulta encontrada para este paciente.")

def menu_relatorios(medico_id):
    print("==== RELATÓRIOS MÉDICO ====")
    while True:
        print("\n=== RELATÓRIOS DO MÉDICO ===")
        print("1 - Total de atendimentos")
        print("2 - Pacientes atendidos no mês")
        print("3 - Consultas pendentes")
        print("0 - Voltar")

        op = input("Escolha uma opção: ").strip()

        if op == '1':
            relatorio_total_atendimentos(medico_id)
        elif op == '2':
            relatorio_pacientes_no_mes(medico_id)
        elif op == '3':
            relatorio_consultas_pendentes(medico_id)
        elif op == '0':
            break
        else:
            print("Opção inválida.")

def relatorio_total_atendimentos(medico_id):
    consultas = ler_json("consultas.json")
    total = sum(1 for c in consultas if c.get('medico_id') == medico_id and c.get('status') == 'Finalizada')
    print(f"\nTotal de atendimentos finalizados: {total}")


def relatorio_pacientes_no_mes(medico_id):
    consultas = ler_json("consultas.json")
    mes_atual = str(date.today())[:7]
    pacientes_ids = set(
        c.get('paciente_id') for c in consultas
        if c.get('medico_id') == medico_id
        and c.get('status') == 'Finalizada'
        and c.get('data', '').startswith(mes_atual)
    )
    print(f"\nPacientes distintos atendidos no mês: {len(pacientes_ids)}")
    for pid in pacientes_ids:
        print(f"  - {resolver_nome_paciente(pid)}")


def relatorio_consultas_pendentes(medico_id):
    consultas = ler_json("consultas.json")
    print("\nConsultas pendentes:")
    encontrou = False
    for c in sorted(consultas, key=lambda x: (x.get('data', ''), x.get('horario', ''))):
        if c.get('medico_id') == medico_id and c.get('status') in ('Agendada', 'Confirmada'):
            encontrou = True
            paciente_nome = resolver_nome_paciente(c.get('paciente_id'))
            print(f"  Data: {c.get('data')} | Horário: {c.get('horario')} | Paciente: {paciente_nome}")
    if not encontrou:
        print("Nenhuma consulta pendente.")
