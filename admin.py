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
    
def listar_usuarios():
    print("=== LISTA DE USUÁRIOS ===")

    usuarios= ler_json('usuarios.json')

    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return False
    
    for u in usuarios:
        status= "Ativo" if u['ativo'] else "Inativo"
        print(f"ID: {u['id']} | {u['nome']} | {u['login']} | {u['perfil']} | {status}")

def cadastrar_medico():
    print("===CADASTRO MEDICO===")
    nome= input("Nome Completo:")
    CRM= input("CRM:")
    especialidade= input("Especialidades:")

    with open ("medicos.json" , "r", encoding="utf-8") as f:
        medicos = json.load(f)
        medico_id = max([m["id"] for m in medicos], default=0) + 1
        novo_medico = {
            "id": medico_id,
            "nome": nome,
            "CRM": CRM,
            "especialidade": especialidade
        }
        medicos.append(novo_medico)

    with open("medicos.json", "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)   

def editar_medico():
    print("===EDITAR MEDICO===")

    id = int(input("ID do Médico a Editar:"))
    
    with open("medicos.json", "r", encoding="utf-8") as f:
        medicos = json.load(f)
        medico = next((m for m in medicos if m["id"] == id), None)
        if not medico:
            print(f"Médico com ID {id} não encontrado.")
        
            return
        
        print(f"Editando Médico: {medico['nome']} (ID: {medico['id']})")
    
        nome = input(f"Novo Nome (deixe em branco para manter '{medico['nome']}'): ")
        CRM = input(f"Novo CRM (deixe em branco para manter '{medico['CRM']}'): ")
        especialidade = input(f"Nova Especialidade (deixe em branco para manter '{medico['especialidade']}'): ")
        
        if nome:
            medico["nome"] = nome
        if CRM:
            medico["CRM"] = CRM
        if especialidade:
            medico["especialidade"] = especialidade

    with open("medicos.json", "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)


def excluir_medico():
    print("===EXCLUIR MEDICO===")

    id = int(input("ID do Médico a Excluir:"))
    
    with open("medicos.json", "r", encoding="utf-8") as f:
        medicos = json.load(f)
        medico = next((m for m in medicos if m["id"] == id), None)
        if not medico:
            print(f"Médico com ID {id} não encontrado.")
            return
        
        medicos.remove(medico)
        print(f"Médico '{medico['nome']}' (ID: {medico['id']}) excluído com sucesso.")

    with open("medicos.json", "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)