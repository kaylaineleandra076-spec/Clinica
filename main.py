from auth import fazer_login, encerrar_sessao, gerar_relatorios, verificar_permissao
import admin
import recepcionista
import medico

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
        admin.cadastrar_usuario()
    elif op == '2':
        admin.editar_usuario()
    elif op == '3':
        admin.excluir_usuario()
    elif op == '4':
        admin.resetar_usuarios()
    elif op == '5':
        admin.listar_usuarios()
    elif op == '6':
        admin.cadastrar_medico()
    elif op == '7':
        admin.editar_medico()
    elif op == '8':
        admin.excluir_medico()
    elif op == '9':
        admin.listar_medicos()
    elif op == '10':
        gerar_relatorios()
    elif op == '0':
        encerrar_sessao()

def menu_recepcionista(usuario):
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

    recepcionista.painel_recepcionista(usuario)

def menu_medico(usuario):
    print("=== MENU MÉDICO ===")
    print("1 - Ver agenda de hoje")
    print("2 - Iniciar atendimento")
    print("0 - Sair")

    op= input("\nEscolha uma opção").strip()

    if op == '1':
        medico.ver_agenda_hoje(usuario)
    elif op == '2':
        medico.iniciar_atendimento(usuario)
    elif op == '0':
        encerrar_sessao()
    else:
        print("Opção inválida. Tente novamente.")


def main():
        
        usuario_logado = fazer_login()
        if not usuario_logado:
            tentar = input('\nDeseja tentar login novamente? (s/n): ').strip().lower()
            if tentar != 's':
                print('Saindo.')
                return

        print('Acesso Liberado!')

        perfil = usuario_logado.get('perfil')
        if perfil == 'administrador':
            menu_administrador()
        elif perfil == 'recepcionista':
            menu_recepcionista(usuario_logado)
        elif perfil == 'medico':
            menu_medico(usuario_logado)
        else:
            print('Perfil desconhecido. Encerrando sessão.')
            encerrar_sessao()