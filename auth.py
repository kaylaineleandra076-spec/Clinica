import json
from pathlib import Path
base = Path(__file__).parent
from banco import ler_json , salvar_json

def ler_json(arquivo):
    caminho= base / arquivo
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def fazer_login():
    login= input("Digite seu login: ")
    senha= input("Digite a senha: ")

    usuarios = ler_json('usuario.json')

    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            if usuario['ativo']:
                print(f'\nBem vindo(a), {usuario['nome']}! Perfil:{usuario['perfil']}.')
                return usuario
            else:
                print("Usuario inativo! Contate o administrador!")
                return None
            
    print("Login ou Senha incorreto!")
    return None

while True:
    usuario_logado= fazer_login()

    if usuario_logado:
        print("Acesso Liberado!")
        break

def verificar_permissao(usuario_logado, perfil_necessario):
    if usuario_logado is None:
        print("ERRO! nenhum usuario logado!")
        return False
    if usuario_logado['perfil']== perfil_necessario:
        return True
    else:
        print(f"Acesso negado. Apenas '{perfil_necessario}' pode acessar esta função!")
        return False
    

def resetar_senha(login):
    usuarios= ler_json['usuarios.json']

    for usuario in usuarios:
        
        if usuario['login'] == login:
            nova_senha= input("Digite uma nova senha: ")
            confirmacao= input("Confirme a nova senha: ")

            if nova_senha != confirmacao:
                print("As senhas não coincidem. Tente novamente.")
                return False
            
            usuario['senha']== nova_senha
            salvar_json('usuarios.json', usuarios)
            print(f"Senha do usuário '{usuario['nome']}' redefinida com sucesso!")
            return True
    
    print(f"Usuario com o login '{login}' não encontrado.")
    return False


def encerrar_sessao():
    global usuario_logado
    nome= usuario_logado['nome']
    usuario_logado= None
    print(f"\n Até logo, {nome}! Sessão encerrada.")

def verificar_permissao(usuario_logado, perfil_necessario):

    if usuario_logado is None:
        print("Nenhum usuario logado!")
        return False
    if isinstance(perfil_necessario, str):
        perfil_necessario = [perfil_necessario]

    if usuario_logado['perfil'] == 'administrador':
        return True
    else:
        print(f"Acesso negado. Apenas {perfil_necessario} pode acessar esta função!")
        return False
    
def resetar_senha(login):
    usuarios= ler_json('usuarios.json')

    for usuario in usuarios:

        if usuario['login'] == login:
            nova_senha= input("Digite uma nova senha: ")
            confirmacao= input("Confirme a nova senha: ")

            if nova_senha != confirmacao:
                print("As senhas não coincidem. Tente novamente.")
                return False
            
            usuario['senha']= nova_senha
            salvar_json('usuarios.json', usuarios)
            print(f"Senha do usuário '{usuario['nome']}' redefinida com sucesso!")
            return True
        
    print(f"Usuario com o login '{login}' não encontrado.")
    return False