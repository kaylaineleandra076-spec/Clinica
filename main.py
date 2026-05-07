from auth import fazer_login, encerrar_sessao, gerar_relatorios, verificar_permissao
from admin import cadastrar_medico, cadastrar_usuario, editar_medico, editar_usuario, excluir_medico, excluir_usuario, listar_medicos, resetar_usuarios, listar_usuarios
from recepcionista import buscar_paciente, cadastrar_paciente, cancelar_consulta, confirmar_presença, consultas_do_dia , editar_paciente, listar_pacientes , encerrar_sessao, marcar_consulta, reagendar_consulta
from medico import ver_agenda_hoje, iniciar_atendimento

def menu_administrador():
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

def menu_recepcionista():
    print("=== MENU RECEPCIONISTA ===")
    print("1 - Cadastrar paciente")
    print("2 - Editar Paciente")
    print("3 - Buscar Pacientes")
    print("4 - Listar Pacientes")
    print("5 - Marcar Consulta")
    print("6 - Reagendar Consulta")
    print("7 - Cancelar Consulta")
    print("8 - Confirmar presença")
    print("9 - Consultas do dia")
    print("10 - Relatorio")
    print("0 - Sair")

    op= input("\nEscolha uma opção").strip()

    if op == '1':
        cadastrar_paciente()
    elif op == '2':
        editar_paciente()
    elif op == '3':
        buscar_paciente()
    elif op == '4':
        listar_pacientes()
    elif op == '5':
        marcar_consulta()
    elif op == '6':
        reagendar_consulta()
    elif op == '7':
        cancelar_consulta()
    elif op == '8':
        confirmar_presença()
    elif op == '9':
        consultas_do_dia()
    elif op == '10':
        menu_relatorio_recepcionista(usuario) # pyright: ignore[reportUndefinedVariable]
    elif op == '0':
        encerrar_sessao()
        exit()
    else:
        print("Opção inválida")

def menu_medico(usuario):
    print("=== MENU MÉDICO ===")
    print("1 - Ver agenda de hoje")
    print("2 - Iniciar atendimento")
    print("0 - Sair")

    op= input("\nEscolha uma opção").strip()

    if op == '1':
        ver_agenda_hoje(usuario)
    elif op == '2':
        iniciar_atendimento(usuario)
    elif op == '0':
        encerrar_sessao(usuario)
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        usuario_logado = fazer_login()

        if usuario_logado:
            print("Acesso Liberado!")
            break

    while True:
        if usuario_logado['perfil'] == 'administrador':
            menu_administrador(usuario_logado)
        elif usuario_logado['perfil'] == 'recepcionista':
            menu_recepcionista(usuario_logado)
        elif usuario_logado['perfil'] == 'medico':
            menu_medico(usuario_logado)
        else:
            print("Perfil desconhecido. Encerrando sessão.")
            encerrar_sessao()
            break