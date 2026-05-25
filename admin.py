import json
from pathlib import Path

base = Path(__file__).parent
from banco import ler_json, gerar_id, salvar_json

def menu_relatorios():
    print("=== RELATÓRIOS ===")
    print("1 - Consultas por período")
    print("2 - Consultas canceladas")
    print("3 - Pacientes cadastrados")
    print("4 - Médicos ativos")
    print("5 - Consultas por médico")
    print("6 - Atendimentos do dia")
    print("7 - Pacientes mais atendidos")
    print("0 - Voltar")

    op = input("\nEscolha uma opção: ").strip()

    if op == '1':
        data_inicial = input("Data inicial (YYYY-MM-DD): ")
        data_final = input("Data final (YYYY-MM-DD): ")
        relatorio = relatorio_consulta_por_periodo(data_inicial, data_final)
        for consulta in relatorio:
            print(consulta)
    elif op == '2':
        relatorio_consultas_canceladas()
    elif op == '3':
        relatorio_pacientes_cadastrados()
    elif op == '4':
        relatorio_medicos_ativos()
    elif op == '5':
        medico_id = int(input("ID do médico: "))
        relatorio = relatorio_consulta_por_medico(medico_id)
        for consulta in relatorio:
            print(consulta)
    elif op == '6':
        relatorio_atendimento_do_dia()
    elif op == '7':
        relatorio_pacientes_mais_atendidos()
    elif op == '0':
        return
    else:
        print("Opção inválida. Tente novamente.")

def cadastrar_usuario():

    print("=== CADASTRO USUÁRIOS ===")

    nome= input("Nome Completo: ")
    login= input("login: ")

    usuarios = ler_json('usuarios.json')

    for usuario in usuarios:
        if usuario['login']== login:
            print(f"ERRO! O login '{login}' já está em uso.")
            return False
    
    senha= input("Digite a senha: ")

    print("\n Perfis disponíveis:")
    print("1 - Administrador")
    print("2 - Recepcionista")
    print("3 - Médico")

    op= input("Digite a opção que deseja: ")

    perfis = {
        '1': 'administrador',
        '2': 'recepcionista',
        '3': 'medico'
    }

    if op not in perfis:
        print("Opção inválida!")
        return False
    
    perfil= perfis[op]

    novo_id= gerar_id('usuarios.json')

    novo_usuario= {
        'id': novo_id,
        'nome': nome,
        'login': login,
        'senha': senha,
        'perfil': perfil,
        'ativo': True
    }

    usuarios.append(novo_usuario)
    salvar_json('usuarios.json', usuarios)

    print(f"\n Usuário '{nome}' cadastrado com sucesso! ID: {novo_id}")
    return True

def editar_usuario():
    print("=== EDITAR USUÁRIO ===")

    usuarios= ler_json('usuarios.json')

    if not usuarios:
        print("Nenhum usuario cadastrado ")
        return False
    
    for u in usuarios:
        status= "Ativo" if u['ativo'] else "Inativo"
        print(f"ID: {u['id']} | {u['nome']} | {u['login']} | {u['perfil']} | {status}")

        id_alvo= input("\n Digite o ID do usuário que deseja editar: ").strip()
        usuario = next((u for u in usuarios if u['id'] == id_alvo), None)

        if not usuario:
            print("Usuario não encontrado!")
            return
        
        print("\nDeixe em branco para mostrar o valor atual.")
        nome= input(f"Nome ({usuario['nome']}): ").strip()
        login= input(f"Login ({usuario['login']}): ").strip()
        perfil= input(f"Perfil ({usuario['perfil']}): ").strip()
        ativo= input(f"Ativo (s/n) ({'s' if usuario['ativo'] else 'n'}): ").strip().lower()

        if nome:
            usuario['nome'] = nome
        if login:
            usuario['login'] = login
        if perfil:
            usuario['perfil'] = perfil
        if ativo == 's':
            usuario['ativo'] = True
        elif ativo == 'n':
            usuario['ativo'] = False
        salvar_json('usuarios.json', usuarios)
        print(f"\n Usuario '{usuario['nome']}' atualizado com sucesso!")

def excluir_usuario():

    print("=== EXCLUIR USUARIO === ")
        
    usuarios= ler_json('usuarios.json')

    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return False
    
    for u in usuarios:
        status= "Ativo" if u['ativo'] else "Inativo"
        print(f"ID: {u['id']} | {u['nome']} | {u['login']} | {u['perfil']} | {status}")

    id_alvo= input("\nDigite o ID do usuário que deseja excluir: ").strip()

    for i, usuario in enumerate(usuarios):
        if usuario['id'] == id_alvo:
            del usuarios[i]
            salvar_json('usuarios.json', usuarios)
            print(f"Usuário '{usuario['nome']}' excluído com sucesso!")
            return True

    print("Usuário não encontrado!")
    return False

def listar_usuarios():
        print("=== LISTA DE USUÁRIOS ===")

        usuarios= ler_json('usuarios.json')

        if not usuarios:
            print("Nenhum usuário cadastrado!")
            return False
        
        for u in usuarios:
            status= "Ativo" if u['ativo'] else "Inativo"
            print(f"ID: {u['id']} | {u['nome']} | {u['login']} | {u['perfil']} | {status}")

def resetar_senha_usuarios():
    print("=== RESETEAR USUÁRIOS ===")
    login= input("Digite o login do usuário para resetar a senha: ").strip()
    usuarios= ler_json('usuarios.json')

    for usuario in usuarios:
        if usuario.get['login'] == login:
            nova_senha= input('Digite a nova senha: ').strip()
            confirmacao= input("Confirme a nova senha: ").strip()
            if nova_senha != confirmacao:
                print("As senhas não coincidem. Operação cancelada.")
                return False
            usuario['senha'] = nova_senha
            salvar_json('usuarios.json', usuarios)
            print(f"Senha do usuário '{usuario['nome']}' resetada com sucesso!")
            return True
# MÉDICOS   


def cadastrar_medico():
    print("=== CADASTRO MÉDICO ===")

    medicos = ler_json('medicos.json')

    nome = input("Nome Completo: ")
    crm = input("CRM: ")
    especialidade = input("Especialidade: ")

    medico_id = gerar_id('medicos.json')

    novo_medico = {
        "id": medico_id,
        "nome": nome,
        "crm": crm,
        "especialidade": especialidade,
        "ativo": True
    }
    medicos = ler_json('medicos.json')
    medicos.append(novo_medico)
    salvar_json('medicos.json', medicos)

    print("Médico cadastrado com sucesso!")

def listar_medicos():
    print("=== LISTA DE MÉDICOS ===")

    medicos = ler_json('medicos.json')
   

    if not medicos:
        print("Nenhum médico cadastrado.")
        return

    for medico in medicos:
        status = "Ativo" if medico["ativo"] else "Inativo"

        print(
            f'ID: {medico["id"]} | '
            f'Nome: {medico["nome"]} | '
            f'CRM: {medico["crm"]} | '
            f'Especialidade: {medico["especialidade"]} | '
            f'Status: {status}'
        )

def editar_medico():
    print("=== EDITAR MÉDICO ===")

    medicos = ler_json('medicos.json')
    listar_medicos()

    try:
        id_medico = int(input("ID do Médico a Editar: "))
    except ValueError:
        print("ID inválido.")
        return

    medico = next((m for m in medicos if m["id"] == id_medico), None)

    if not medico:
        print(f"Médico com ID {id_medico} não encontrado.")
        return

    nome = input(f"Novo Nome ({medico['nome']}): ")
    crm = input(f"Novo CRM ({medico['crm']}): ")
    especialidade = input(f"Nova Especialidade ({medico['especialidade']}): ")

    ativo = input("Médico ativo? (s/n): ").lower()

    if nome:
        medico["nome"] = nome

    if crm:
        medico["crm"] = crm

    if especialidade:
        medico["especialidade"] = especialidade

    if ativo == "s":
        medico["ativo"] = True

    elif ativo == "n":
        medico["ativo"] = False

    salvar_json('medicos.json', medicos)

    print("Médico atualizado com sucesso!")

def excluir_medico():
    print("=== EXCLUIR MÉDICO ===")
    medicos = ler_json('medicos.json')
    listar_medicos()
    
    try:
        id_medico = int(input("ID do Médico a Excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    medico = next((m for m in medicos if m["id"] == id_medico), None)

    if not medico:
        print(f"Médico com ID {id_medico} não encontrado.")
        return

    confirmar = input(
        f'Tem certeza que deseja excluir "{medico["nome"]}"? (s/n): '
    ).lower()

    if confirmar == "s":
        medicos.remove(medico)
        salvar_json('medicos.json', medicos)
        print("Médico excluído com sucesso!")
    else:
        print("Exclusão cancelada.")

#CONSULTAS
def relatorio_consulta_por_periodo(data_inicial, data_final):
    consultas = ler_json("consultas.json")
    relatorio = []
    for consulta in consultas:
        if data_inicial <= consulta["data"] <= data_final:
            relatorio.append(consulta)
    return relatorio

def relatorio_consultas_canceladas():
    consultas = ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")
    medicos = ler_json("medicos.json")

    canceladas = [c for c in consultas if c["status"] == "Cancelada"]

    if not canceladas:
        print("Nenhuma consulta cancelada anteriormente.") 
        return
    
    print(f"\nTotal: {len(canceladas)} consultas canceladas.\n")
    for consulta in canceladas:
        paciente = next((p for p in pacientes if p["id"] == consulta["paciente_id"]), None)
        medico = next((m for m in medicos if m["id"] == consulta["medico_id"]), None)

        nome_paciente = paciente["nome"] if paciente else "Paciente Desconhecido"
        nome_medico = medico["nome"] if medico else "Médico Desconhecido"

        print(f"Consulta ID: {consulta['id']}, Paciente: {nome_paciente}, Médico: {nome_medico}, Data: {consulta['data']}, Horário: {consulta['horario']}")

def relatorio_pacientes_cadastrados():
    print("=== PACIENTES CADASTRADOS ===")

    pacientes = ler_json('pacientes.json')
    print(f"Total de pacientes cadastrados: {len(pacientes)}")


def relatorio_medicos_ativos():
    print("=== MÉDICOS ATIVOS ===")
    medicos = ler_json('medicos.json')
    ativos = [m for m in medicos if m.get('ativo', True)]
    print(f"Total de médicos ativos: {len(ativos)}")

def relatorio_consulta_por_medico(medico_id):
    consultas = ler_json("consultas.json")
    relatorio = []
    for consulta in consultas:
        if consulta["medico_id"] == medico_id:
            relatorio.append(consulta)
    return relatorio

def relatorio_atendimento_do_dia():
    print("=== ATENDIMENTOS DO DIA ===")

    from datetime import date
    hoje = str(date.today())

    consultas = ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")
    medicos = ler_json('medicos.json')

    hoje_consultas = [c for c in consultas if c['data'] == hoje]
    
    if not hoje_consultas:
        print("Nenhuma consulta agendada para hoje.")
        return
    print(f"Total: {len(hoje_consultas)} consulta(s).")

    for c in sorted(hoje_consultas, key= lambda x: x['horario']):
        paciente = next((p for p in pacientes if p['id'] == c['pacientes_id']), None)
        medico = next((m for m in medicos  if m['id'] == c['medico_id']), None)
        nome_paciente= paciente['nome'] if paciente else "Paciente Desconhecido"
        nome_medico= medico['nome'] if medico else "Médico Desconhecido"
        print(f"Horário: {c['horario']} | Paciente: {nome_paciente} | Médico: {nome_medico} | Status: {c['status']}")

def relatorio_pacientes_mais_atendidos():
    print("=== PACIENTES MAIS ATENDIDOS ===")

    consultas = ler_json("consultas.json")
    pacientes = ler_json("pacientes.json")

    finalizadas= [c for c in consultas if c['status'] == 'Finalizada']

    if not finalizadas:
        print("Nenhuma consulta finalizada.")
        return
    
    contagem = {}

    for c in finalizadas:
        contagem[c['paciente_id']] = contagem.get(c['paciente_id'], 0) + 1

    ranking= sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    for i, (pid, total) in enumerate(ranking, start=1):
            paciente = next((p for p in pacientes if p['id'] == pid), None)
            print(f"{i}. {paciente['nome']} | {total} atendimentos")