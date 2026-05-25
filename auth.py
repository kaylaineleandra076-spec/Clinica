from banco import ler_json , salvar_json

def fazer_login():
    print("=== LOGIN ===")
    login= input("Digite seu login: ").strip()
    senha= input("Digite a senha: ").strip()

    usuarios = ler_json('usuarios.json')

    for usuario in usuarios:
        if usuario.get('login') == login and usuario.get('senha') == senha:
            if usuario.get('ativo', True):
                print(f"\nBem vindo(a), {usuario['nome']}! Perfil: {usuario['perfil']}.")
                return usuario
            else:
                print("Usuario inativo! Contate o administrador!")
                return None
            
    print("Login ou Senha incorreto!")
    return None

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
    usuarios = ler_json('usuarios.json')
    for usuario in usuarios:
        if usuario.get('login') == login:
            nova_senha = input("Digite uma nova senha: ").strip()
            confirmacao = input("Confirme a nova senha: ").strip()
            if nova_senha != confirmacao:
                print("As senhas não coincidem. Tente novamente.")
                return False
            usuario['senha'] = nova_senha
            salvar_json('usuarios.json', usuarios)
            print(f"Senha do usuário '{usuario['nome']}' redefinida com sucesso!")
            return True
    print(f"Usuario com o login '{login}' não encontrado.")
    return False


def encerrar_sessao(usuario=None):
    if usuario and isinstance(usuario, dict):
        nome = usuario.get('nome')
        print(f"\nAté logo, {nome}! Sessão encerrada.")
    else:
        print("\nSessão encerrada.")