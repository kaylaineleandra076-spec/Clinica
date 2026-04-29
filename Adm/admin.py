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
        print("Nenhum usuario ")
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
            break
        