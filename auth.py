import json
from pathlib import Path
base = Path(__file__).parent
from banco import ler_json , salvar_json

def ler_json(arquivo):
    caminho= base / arquivo
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)
def salvar_json(arquivo, dados):
    caminho= base / arquivo
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def fazer_login():
    login= input("Digite seu login: ")
    senha= input("Digite a senha: ")

    usuarios = ler_json('usuario.json')

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

# NOTE: não executar loop de login no import — `main.py` gerencia o fluxo de execução

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
            nova_senha = input("Digite uma nova senha: ")
            confirmacao = input("Confirme a nova senha: ")
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


# NOTE: não executar loop de login no import — `main.py` gerencia o fluxo de execução

def gerar_relatorios():
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
