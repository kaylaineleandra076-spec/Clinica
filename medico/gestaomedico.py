import json
import os

# ==================== FUNCOES AUXILIARES ====================

def carregar_medicos():
    """Le os medicos do arquivo medicos.json"""
    if not os.path.exists("medicos.json"):
        # Se o arquivo nao existe, cria um vazio
        return []
    
    with open("medicos.json", "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_medicos(medicos):
    """Salva os medicos no arquivo medicos.json"""
    with open("medicos.json", "w", encoding="utf-8") as f:
        json.dump(medicos, f, indent=4, ensure_ascii=False)


# ==================== FUNCIONALIDADES ====================

def cadastrar_medico():
    """Adiciona um novo medico ao sistema"""
    print("\n===== CADASTRAR MEDICO =====")
    
    # Pede os dados do medico
    nome = input("Digite o nome do medico: ")
    crm = input("Digite o CRM: ")
    especialidade = input("Digite a especialidade: ")
    
    # Carrega os medicos ja cadastrados
    medicos = carregar_medicos()
    
    # Gera um ID automatico (pega o maior ID e soma 1)
    if len(medicos) == 0:
        novo_id = 1
    else:
        novo_id = medicos[-1]["id"] + 1
    
    # Cria o novo medico
    novo_medico = {
        "id": novo_id,
        "nome": nome,
        "crm": crm,
        "especialidade": especialidade,
        "ativo": True  # Comeca sempre ativo
    }
    
    # Adiciona a lista
    medicos.append(novo_medico)
    
    # Salva no arquivo
    salvar_medicos(medicos)
    
    print(f"Medico '{nome}' cadastrado com sucesso! ID: {novo_id}")


def listar_medicos():
    """Mostra todos os medicos cadastrados em forma de tabela"""
    print("\n===== LISTAR MEDICOS =====")
    
    medicos = carregar_medicos()
    
    if len(medicos) == 0:
        print("Nenhum medico cadastrado!")
        return
    
    # Cabecalho da tabela
    print("\n" + "-" * 80)
    print(f"{'ID':<5} {'NOME':<25} {'CRM':<10} {'ESPECIALIDADE':<20} {'STATUS':<10}")
    print("-" * 80)
    
    # Mostra cada medico
    for medico in medicos:
        status = "ATIVO" if medico["ativo"] else "INATIVO"
        print(f"{medico['id']:<5} {medico['nome']:<25} {medico['crm']:<10} {medico['especialidade']:<20} {status:<10}")
    
    print("-" * 80)
    print(f"Total de medicos: {len(medicos)}\n")


def editar_medico():
    """Edita um medico existente"""
    print("\n===== EDITAR MEDICO =====")
    
    # Primeiro mostra os medicos
    listar_medicos()
    
    medicos = carregar_medicos()
    
    if len(medicos) == 0:
        return
    
    # Pede qual medico quer editar
    try:
        id_medico = int(input("Digite o ID do medico que deseja editar: "))
    except ValueError:
        print("ID deve ser um numero!")
        return
    
    # Procura o medico
    medico_encontrado = None
    for med in medicos:
        if med["id"] == id_medico:
            medico_encontrado = med
            break
    
    if medico_encontrado is None:
        print(f"Medico com ID {id_medico} nao encontrado!")
        return
    
    print(f"\nEditando: {medico_encontrado['nome']}")
    print("-" * 40)
    
    # Menu de edicao
    while True:
        print("\nO que deseja editar?")
        print("1. Nome")
        print("2. CRM")
        print("3. Especialidade")
        print("4. Status (Ativo/Inativo)")
        print("5. Salvar e Sair")
        
        opcao = input("Escolha (1-5): ")
        
        if opcao == "1":
            novo_nome = input("Digite o novo nome: ")
            medico_encontrado["nome"] = novo_nome
            print("Nome atualizado!")
        
        elif opcao == "2":
            novo_crm = input("Digite o novo CRM: ")
            medico_encontrado["crm"] = novo_crm
            print("CRM atualizado!")
        
        elif opcao == "3":
            nova_especialidade = input("Digite a nova especialidade: ")
            medico_encontrado["especialidade"] = nova_especialidade
            print("Especialidade atualizada!")
        
        elif opcao == "4":
            if medico_encontrado["ativo"]:
                print("Status atual: ATIVO")
                desativar = input("Desativar? (S/N): ").upper()
                if desativar == "S":
                    medico_encontrado["ativo"] = False
                    print("Medico marcado como INATIVO!")
            else:
                print("Status atual: INATIVO")
                ativar = input("Ativar? (S/N): ").upper()
                if ativar == "S":
                    medico_encontrado["ativo"] = True
                    print("Medico marcado como ATIVO!")
        
        elif opcao == "5":
            salvar_medicos(medicos)
            print("Alteracoes salvas com sucesso!")
            break
        
        else:
            print("Opcao invalida!")


def excluir_medico():
    """Remove um medico do sistema"""
    print("\n===== EXCLUIR MEDICO =====")
    
    # Primeiro mostra os medicos
    listar_medicos()
    
    medicos = carregar_medicos()
    
    if len(medicos) == 0:
        return
    
    # Pede qual medico quer excluir
    try:
        id_medico = int(input("Digite o ID do medico que deseja excluir: "))
    except ValueError:
        print("ID deve ser um numero!")
        return
    
    # Procura o medico
    medico_encontrado = None
    for med in medicos:
        if med["id"] == id_medico:
            medico_encontrado = med
            break
    
    if medico_encontrado is None:
        print(f"Medico com ID {id_medico} nao encontrado!")
        return
    
    # Pede confirmacao
    print(f"\nTem certeza que deseja excluir '{medico_encontrado['nome']}'?")
    confirmacao = input("Digite SIM para confirmar: ").upper()
    
    if confirmacao == "SIM":
        medicos.remove(medico_encontrado)
        salvar_medicos(medicos)
        print(f"Medico '{medico_encontrado['nome']}' foi excluido!")
    else:
        print("Exclusao cancelada!")


# ==================== MENU PRINCIPAL ====================

def menu():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*50)
        print("       SISTEMA DE GESTAO DE MEDICOS")
        print("="*50)
        print("1. Cadastrar Medico")
        print("2. Listar Medicos")
        print("3. Editar Medico")
        print("4. Excluir Medico")
        print("0. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            cadastrar_medico()
        elif opcao == "2":
            listar_medicos()
        elif opcao == "3":
            editar_medico()
        elif opcao == "4":
            excluir_medico()
        elif opcao == "0":
            print("\nAte logo!")
            break
        else:
            print("Opcao invalida! Tente novamente.")


# ==================== INICIAR PROGRAMA ====================

if __name__ == "__main__":
    menu()