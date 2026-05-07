import json
from pathlib import Path
base = Path(__file__).parent
from banco import ler_json,gerar_id,salvar_json

def cadastrar_usuario():

    print("=== CADASTRO USUÁRIOS ===")

    nome= input("Nome Completo: ")
    login= input("login: ")

    usuarios = ler_json('usuariod.json')

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

    novo_id= gerar_id(usuarios)

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

        usuario_encontrado = None
        for usuario in usuarios: 
            if usuario['id'] == id_alvo:
                usuario_encontrado = usuario
                break

        if not usuario_encontrado:
            print("Usuario não encontrado!")
            False
        
        
        print("\nDeixe em branco para mostrar o valor atual.")

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

def resetar_usuarios():
    print("=== RESETEAR USUÁRIOS ===")
    confirmacao= input("Tem certeza que deseja resetar os usuários? Todos os dados serão perdidos! (s/n): ").strip().lower()

    if confirmacao == 's':
        salvar_json('usuarios.json', [])
        print("Todos os usuários foram resetados com sucesso!")
        return True
    else:
        print("Operação cancelada.")
        return False

# MÉDICOS   

def carregar_medicos():
    if not arquivo_medicos.exists():
        return []

    with open(arquivo_medicos, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_medicos(medicos):
    with open(arquivo_medicos, "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)


def cadastrar_medico():
    print("=== CADASTRO MÉDICO ===")

    medicos = carregar_medicos()

    nome = input("Nome Completo: ")
    crm = input("CRM: ")
    especialidade = input("Especialidade: ")

    medico_id = max([m["id"] for m in medicos], default=0) + 1

    novo_medico = {
        "id": medico_id,
        "nome": nome,
        "crm": crm,
        "especialidade": especialidade,
        "ativo": True
    }


    medicos.append(novo_medico)

    salvar_medicos(medicos)

    print("Médico cadastrado com sucesso!")


def listar_medicos():
    print("=== LISTA DE MÉDICOS ===")

    medicos = carregar_medicos()

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

    medicos = carregar_medicos()

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

    salvar_medicos(medicos)

    print("Médico atualizado com sucesso!")


def excluir_medico():
    print("=== EXCLUIR MÉDICO ===")

    medicos = carregar_medicos()

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

        salvar_medicos(medicos)

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

    canceladas = [c for c in consultas if c["status"] == "cancelada"]

    if not canceladas:
        print("Nenhuma consulta cancelada anteriormente.") 
        return
    
    print(f"\nTotal: {len(canceladas)} consultas canceladas.\n")
    for consulta in canceladas:
        paciente = next((p for p in pacientes if p["id"] == consulta["paciente_id"]), None)
        medico = next((m for m in medicos if m["id"] == consulta["medico_id"]), None)

        nome_paciente = paciente["nome"] if paciente else "Paciente Desconecido"
        nome_medico = medico["nome"] if medico else "Médico Desconhecido"

        print(f"Consulta ID: {consulta['id']}, Paciente: {nome_paciente}, Médico: {nome_medico}, Data: {consulta['data']}, Horário: {consulta['horario']}")

def relatorio_pacientes_cadastrados():
    print("=== PACIENTES CADASTRADOS ===")

    pacientes = ler_json('pacientes.json')
    print(f"Total de pacientes cadastrador: {len('pacientes.josn')}")

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

    hoje_consultas = [c for c in consultas if consultas if c['datas'] == hoje]
    
    if not hoje_consultas:
        print("Nenhuma consulta agendada para hoje.")
        return
    print(f"Total: {len(hoje_consultas)} consulta(s).")

    for c in sorted(hoje_consultas, key= lambda x: x['horario']):
        paciente = next((p for p in pacientes if p['id'] == c['pacientes_id']), None)
        medico = next((m for m in medicos  if m['id'] == m['medico_id']), None)

        print(f"{c['horario']} | {paciente['nome']} | Dr(a). {medico['nome']} | {c['status']}")

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