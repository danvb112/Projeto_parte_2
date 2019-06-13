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
            aluno.set_nome(input("Digite o nome: "))
            aluno.set_cpf(input("Digite o cpf: "))
            if  aluno.adicionar_ao_banco():
                print("Aluno Cadastrado com sucesso!")
                alunos_menu()
            else:
                print("Aluno já cadastrado!")
                alunos_menu()
    
        if opcao == "3":
            aluno.set_cpf(input("Digite o cpf: "))
            if aluno.apagar_do_banco():
                print("Aluno não existente")
                alunos_menu()
            else:
                print("Aluno apagado com sucesso")
                alunos_menu()
        
        
        if opcao == "4":
            aluno.set_cpf(input("Digite o cpf: "))
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo cpf: ")
            if not aluno.atualizar_banco(novo_nome, novo_cpf):
                print("Aluno atualizado com sucesso!")
                alunos_menu()
            else:
                print("Aluno não existente!")
                alunos_menu()
        if opcao == "0":
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            alunos_menu()
            continue


def professores_menu():
    print("""

        --- SISTEMA ACADEMICO / PROFESSORES ---    
        ===============================================
        --- Escolha uma opção  ---
        ===============================================

        1 - Listar 
        2 - Adicionar
        3 - Deletar
        4 - Atualizar
        
        0 - Voltar

        ==============================================
                
    """)
    professor = Professor()
    
    while True:
        opcao = input("Digite a opção: ")

        if opcao == "1":
            professor.lsitar()
            professores_menu()
        if opcao == "2":
            professor.set_nome(input("Digite o nome: "))
            professor.set_cpf(input("Digite o cpf: "))
            professor.set_departamento(input("Digite o departamento: "))  
            if professor.adicionar():
                print('\n--- Professor já existe ---\n')
                professores_menu()
            else:
                print("\n--- Professor adicionado com sucesso! ---\n")
                professores_menu()
        if opcao == "3":
            professor.set_cpf(input("Digite o cpf: "))
            if professor.apagar():
                print('\n--- Professor nao existente. ---\n')
                professores_menu()
            else:
                print("\n--- Professor deletado ---\n")
                professores_menu()
        if opcao == "4":
            professor.set_cpf(input("Digite o cpf: "))
            novo_nome = input("Digite o nome atualizado: ")
            novo_cpf = input("Digite o cpf atualizado: ")
            novo_departamento = input("Digite o departamento atualizado: ")
            if professor.atualizar(novo_nome, novo_cpf, novo_departamento):
                print("\n--- Professor não registrado ---")
                professores_menu()
            else:
                print("\n--- Professor atualizado com sucesso ---")
                professores_menu()

        if opcao == "0":
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            professores_menu()
            continue


def disciplina_menu():
    print("""

        --- SISTEMA ACADEMICO / DISCIPLINA ---    
        ===============================================
        --- Escolha uma opção  ---
        ===============================================

        1 - Listar 
        2 - Adicionar
        3 - Deletar
        4 - Atualizar
    
        0 - Voltar

        ==============================================
                
    """)

    disciplina = Disciplina()


    while True:
        opcao = input("Digite a opção: ")

            
        if opcao == '1':
            disciplina.listar() 
            disciplina_menu()
        if opcao == '2':
            disciplina.set_nome(input("Digite o nome: "))
            disciplina.set_codigo(input("Digite o codigo: "))
            if disciplina.adicionar():
                print("\n --- Disciplina já cadastrada! ---\n")
                disciplina_menu()
            else:
                print("\n--- Disciplina cadastrada com sucesso ---\n")
                disciplina_menu()
        if opcao == '3':
            disciplina.set_codigo(input("Digite o codigo: "))
            if disciplina.apagar():
                print(("\n--- Disciplina não cadastrada ---\n"))
                disciplina_menu()
            else:
                print("\n--- Disciplina deletada ---\n")
                disciplina_menu()
        if opcao == '4':
            disciplina.set_codigo(input("Digite o codigo: "))
            novo_nome = input("Digite o nome atualizado: ")
            novo_codigo = input("Digite o codigo atualizado: ")
            if not disciplina.atualizar(novo_nome, novo_codigo):
                print("\n--- Disciplina Atualizada ---\n")
                disciplina_menu()
            else:
                print("\n--- Disciplina não cadastrada ---\n")
                disciplina_menu()
        if opcao == '0':
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            disciplina_menu()
            continue

