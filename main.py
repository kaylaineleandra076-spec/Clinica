from auth import fazer_login, verificar_permissao, encerrar_sessao, resetar_senha, logi
from admin import cadastrar_usuario, editar_usuario, excluir_usuario, resetar_usuarios, listar_usuarios
from recepcionista import cadastrar_paciente, editar_paciente
from medico import ver_agenda_hoje, iniciar_atendimento

def menu_administrador(usuario):
    print("=== MENU ADMINISTRADOR === ")
    print("1 - Cadastrar usuário")
    print("2 - Editar usuário")
    print("3 - Excluiur usuario")
    print("4 - Resetar senha de usuario")
    print("5 - Listar usuarios")
    print("6 - Cadastrar médico")
    print("7 - Editar médico")
    print("8 - Excluir médico")
    print("9 - Listar médicos")
    print("10 - Relatórios")
    print("0 - Sair")

    op= input("\nEscolha uma opção").strip()

    if op == '1':
        cadastrar_usuario()
    elif op == '2':
        editar_usuario()
    elif op == '3':
        excluir_usuario()
    elif op == '4':
        resetar_usuarios()
    elif op == '5':
        listar_usuarios()
    elif op == '6':
        cadastrar_medico()
    elif op == '7':
        editar_medico()
    elif op == '8':
        excluir_medico()
    elif op == '9':
        listar_medicos()
    elif op == '10':
        gerar_relatorios()
    elif op == '0':
        encerrar_sessao()
    else:
        print("Opção inválida. Tente novamente.")