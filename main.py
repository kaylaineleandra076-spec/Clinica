from auth import fazer_login, encerrar_sessao, verificar_permissao
import admin
import recepcionista
import medico

def menu_administrador():
    while True:
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

        op= input("\nEscolha uma opção: ").strip()

        if op == '1':
            admin.cadastrar_usuario()
        elif op == '2':
            admin.editar_usuario()
        elif op == '3':
            admin.excluir_usuario()
        elif op == '4':
            admin.resetar_senha_usuarios()
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
            admin.menu_relatorios()
        elif op == '0':
            encerrar_sessao()
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_recepcionista(usuario):
    while True:
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

        op = input("\nEscolha uma opção: ").strip()

        if op == '1':
            recepcionista.cadastrar_paciente()
        elif op == '2':
            recepcionista.editar_paciente()
        elif op== '3':
            recepcionista.buscar_paciente()
        elif op == '4':
            recepcionista.listar_pacientes()
        elif op == '5':
            recepcionista.marcar_consulta()
        elif op == '6':
            recepcionista.reagendar_consulta()
        elif op == '7':
            recepcionista.cancelar_consulta()
        elif op == '8':
            recepcionista.confirmar_presenca()
        elif op == '9':
            recepcionista.listar_consultas_do_dia()
        elif op == '10':
            recepcionista.menu_relatorios()
        elif op == '0':
            encerrar_sessao()
            break
        else:
            print("Opção inválida. Tente novamente.")
            

def menu_medico(usuario):
    while True:
        print("=== MENU MÉDICO ===")
        print("1 - Ver agenda de hoje")
        print("2 - Ver agenda futura")
        print("3 - Iniciar atendimento")
        print("4 - Finalizar atendimento")
        print("5 - Registrar prontuário")
        print("6 - Ver prontuário do paciente")
        print("7 - Historico do paciente")
        print("8 - Relatórios")
        print("0 - Sair")

        op= input("\nEscolha uma opção: ").strip()

        if op == '1':
            medico.ver_agenda_hoje(usuario['id'])
        elif op == '2':
            medico.ver_agenda_futura(usuario['id'])
        elif op == '3':
            medico.iniciar_atendimento(usuario['id'])
        elif op == '4':
            medico.finalizar_atendimento(usuario['id'])
        elif op == '5':
            medico.registrar_prontuario(usuario['id'])
        elif op == '6':
            medico.ver_prontuarios_paciente(usuario['id'])
        elif op == '7':
            medico.buscar_historico_paciente(usuario['id'])
        elif op == '8':
            medico.menu_relatorios(usuario['id'])
        elif op == '0':
            encerrar_sessao()
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    while True:
        usuario_logado = fazer_login()
        if not usuario_logado:
            tentar = input('\nDeseja tentar login novamente? (s/n): ').strip().lower()
            if tentar != 's':
                print('Saindo.')
                break
            continue

        print('Acesso Liberado!')

        perfil = usuario_logado.get('perfil')
        if perfil == 'administrador' and verificar_permissao(usuario_logado, 'administrador'):
            menu_administrador()
        elif perfil == 'recepcionista' and verificar_permissao(usuario_logado, 'recepcionista'):
            menu_recepcionista(usuario_logado)
        elif perfil == 'medico' and verificar_permissao(usuario_logado, 'medico'):
            menu_medico(usuario_logado)
        else:
            print('Perfil desconhecido ou sem permissão. Encerrando sessão.')
            encerrar_sessao()
            break

if __name__ == "__main__":
    main()
    