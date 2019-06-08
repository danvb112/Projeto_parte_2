from Aluno import Aluno
from Professor import Professor
from Disciplina import Disciplina

def home_menu():
    print("""

        --- MENU ---
        ==============================================
        --- Qual operação você deseja fazer? ---
        ==============================================

        1 - Alunos
        2 - Professores
        3 - Disciplinas
        4 - Turmas
        5 - Relatórios

        0 - Sair

        ==============================================    
  
    """)
    while True:
        opcao_menu = input("Digite a opção: ")
        
        if opcao_menu == "1":
            alunos_menu()
        if opcao_menu == "2":
            professores_menu()
        if opcao_menu == "3":
            disciplina_menu()
        if opcao_menu == "4":
            turma_menu()
        if opcao_menu == "5":
            relatorio_menu()
        if opcao_menu == "0":
            exit()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            home_menu()
            continue
    

def alunos_menu():
    print("""

        --- SISTEMA ACADEMICO / ALUNOS ---    
        ===============================================
        --- Escolha uma opção ---
        ===============================================

        1 - Listar 
        2 - Adicionar
        3 - Deletar
        4 - Atualizar
        5 - Gravar informações
        
        0 - Voltar

        ==============================================
                
    """)

    aluno = Aluno()

    while True:
        opcao = input("Digite a opção: ")
        
        if opcao == "1":
            aluno.listar_todos()
            alunos_menu()
        if opcao == "2":
            aluno.set_cpf(input("Digite o nome: "))
            aluno.set_nome(input("Digite o cpf: "))
            if  not aluno.adicionar_ao_banco():
                print("Aluno já cadastrado!")
                alunos_menu()
            else:
                print("Aluno Cadastrado com sucesso!")
                alunos_menu()
    
        if opcao == "3":
            cpf = helpers.pede_cpf()
            if alunos.apagar(cpf) == True:
                print("\n--- Aluno deletado ---\n")
            else:
                print("\n --- Aluno não cadastrado ---\n")
            alunos_menu()
        if opcao == "4":
            cpf = helpers.pede_cpf()
            if alunos.atualizar(cpf) == True:
                print("\n--- Aluno atualizado ---\n")  
            else:
                print("\n--- Aluno não cadastrado ---\n")
            alunos_menu()
        
        if opcao == "5":
            alunos.salvar()
            alunos_menu()
        if opcao == "0":
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            alunos_menu()
            continue


