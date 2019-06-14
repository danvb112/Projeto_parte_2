from tkinter import *
from Aluno import Aluno
from Professor import Professor
from Disciplina import Disciplina

disciplina = Disciplina()
professor = Professor()
aluno = Aluno()


def home_menu():
    janela_principal = Tk()
    
    lb1 = Label(janela_principal, text="--- MENU ---")
    lb2 = Label(janela_principal, text="==============================================")
    lb3 = Label(janela_principal, text="--- Qual menu você deseja acessar? ---")
    lb4 = Label(janela_principal, text="==============================================")

    bt1 = Button(janela_principal, width=20, text= "Alunos", command= alunos_menu )
    bt2 = Button(janela_principal, width=20, text= "Professores", command= professores_menu )
    bt3 = Button(janela_principal, width=20, text= "Disciplinas", command=  disciplinas_menu )
    bt4 = Button(janela_principal, width=20, text= "Sair", command= exit )

    lb5 = Label(janela_principal, text="==============================================") 

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    lb4.grid(row=3, column=0)

    bt1.grid(row=4, column=0)
    bt2.grid(row=5, column=0)
    bt3.grid(row=6, column=0)
    bt4.grid(row=7, column=0)

    lb5.grid(row=8, column=0)
  
    janela_principal.geometry("")
    janela_principal.mainloop()


def alunos_menu():

    janela_alunos = Tk()

    lb1 = Label(janela_alunos, text="--- SISTEMA ACADEMICO / ALUNOS ---")
    lb2 = Label(janela_alunos, text="===============================================")
    lb3 = Label(janela_alunos, text="--- Escolha uma opção ---")
    lb4 = Label(janela_alunos, text="===============================================")
    
    bt1 = Button(janela_alunos, width= 20, text="Listar")
    bt2 = Button(janela_alunos, width= 20, text="Adicionar", command= janela_adicionar_aluno)
    bt3 = Button(janela_alunos, width= 20, text="Deletar", command=janela_deletar_aluno)
    bt4 = Button(janela_alunos, width= 20, text="Atualizar", command=janela_atualizar_aluno)
  
    lb5 = Label(janela_alunos, text="==============================================")

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    lb4.grid(row=3, column=0)

    bt1.grid(row=4,column=0)
    bt2.grid(row=5,column=0)
    bt3.grid(row=6,column=0)
    bt4.grid(row=7,column=0)

    lb5.grid(row=9,column=0)

    janela_alunos.geometry("")
    janela_alunos.mainloop()


def janela_adicionar_aluno():

    def bt_click():

        nome = entrada_aluno.get()
        cpf = entrada_cpf.get()

        aluno.set_nome(nome)
        aluno.set_cpf(cpf)

        if not aluno.adicionar_ao_banco():
            lb3 = Label(janela, text="Aluno adicionado com sucesso")
            lb3.grid(row=3, column=0, columnspan=2)
        else:
            lb4 = Label(janela, text="Aluno já existente")
            lb4.grid(row=3, column=0, columnspan=2)
    


    janela = Tk()
    
    lb1 = Label(janela, text="Digite o Nome: ")
    lb2 = Label(janela, text="Digite o CPF: ")

    entrada_aluno = Entry(janela)
    entrada_cpf = Entry(janela)

    bt = Button(janela, width= 10, text="confirmar", command= bt_click)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    
    entrada_aluno.grid(row=0, column=1)
    entrada_cpf.grid(row=1, column=1)

    bt.grid(row=2, column=0, columnspan=2)
    
    janela.geometry("")
    janela.mainloop()


def janela_deletar_aluno():

    def bt_click():

        cpf = entrada_cpf.get()
        aluno.set_cpf(cpf)

        if not aluno.apagar_do_banco():
            lb2 = Label(janela, text="Aluno apagado com sucesso")
            lb2.grid(row=2, column=0, columnspan=2)
        else:
            lb3 = Label(janela, text="Aluno não existente")
            lb3.grid(row=2, column=0, columnspan=2)
            

    janela = Tk()
    
    lb1 = Label(janela, text="Digite o CPF: ")

    entrada_cpf = Entry(janela)

    bt = Button(janela, width= 10, text="confirmar", command= bt_click)

    lb1.grid(row=0, column=0)

    entrada_cpf.grid(row=0, column=1)

    bt.grid(row=1, column=0, columnspan=2)
    
    janela.geometry("")
    janela.mainloop()

def janela_atualizar_aluno():

    def bt_click():
        
        cpf = entrada_cpf.get()
        novo_nome = entrada_novo_nome.get()
        novo_cpf = entrada_novo_cpf.get()
        aluno.set_cpf(cpf)

        if  not aluno.atualizar_banco(novo_nome, novo_cpf):
            lb4 = Label(janela, text="Aluno Atualizado com sucesso")
            lb4.grid(row=4, column=0, columnspan=2)
        else:
            lb5 = Label(janela, text="Aluno não existente")
            lb5.grid(row=4, column=0, columnspan=2)



    janela = Tk()
    
    lb1 = Label(janela, text="Digite o CPF: ")
    lb2 = Label(janela, text="Digite o novo Nome: ")
    lb3 = Label(janela, text="Digite o novo Cpf: ") 

    entrada_cpf = Entry(janela)
    entrada_novo_nome = Entry(janela)
    entrada_novo_cpf = Entry(janela)

    bt = Button(janela, width= 10, text="confirmar", command= bt_click)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    
    entrada_cpf.grid(row=0, column=1)
    entrada_novo_nome.grid(row=1, column=1)
    entrada_novo_cpf.grid(row=2, column= 1)

    bt.grid(row=3, column=0, columnspan=2)
    
    janela.geometry("")
    janela.mainloop()



def professores_menu():

    janela_alunos = Tk()

    lb1 = Label(janela_alunos, text="--- SISTEMA ACADEMICO / PROFESSORES ---")
    lb2 = Label(janela_alunos, text="===============================================")
    lb3 = Label(janela_alunos, text="--- Escolha uma opção ---")
    lb4 = Label(janela_alunos, text="===============================================")
    
    bt1 = Button(janela_alunos, width= 20, text="Listar")
    bt2 = Button(janela_alunos, width= 20, text="Adicionar", command= janela_adicionar_professor)
    bt3 = Button(janela_alunos, width= 20, text="Deletar", command= janela_deletar_professor)
    bt4 = Button(janela_alunos, width= 20, text="Atualizar", command= janela_atualizar_professor)
  
    lb5 = Label(janela_alunos, text="==============================================")

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    lb4.grid(row=3, column=0)

    bt1.grid(row=4,column=0)
    bt2.grid(row=5,column=0)
    bt3.grid(row=6,column=0)
    bt4.grid(row=7,column=0)

    lb5.grid(row=9,column=0)

    janela_alunos.geometry("")
    janela_alunos.mainloop()


def janela_adicionar_professor():

    def bt_click():

        nome = entrada_nome.get()
        cpf = entrada_cpf.get()
        departamento = entrada_departamento.get()

        professor.set_nome(nome)
        professor.set_cpf(cpf)
        professor.set_departamento(departamento)
        
        if not professor.adicionar():
            lb4 = Label(janela, text="Professor adicionado")
            lb4.grid(row=4, column=0, columnspan=2)
        else:
            lb5 = Label(janela, text="Professor não existente")
            lb5.grid(row=4, column=0, columnspan=2)
    
    janela = Tk()
    
    lb1 = Label(janela, text="Digite o Nome: ")
    lb2 = Label(janela, text="Digite o CPF: ")
    lb3 = Label(janela, text= "Digite o Departamento: ")

    entrada_nome = Entry(janela)
    entrada_cpf = Entry(janela)
    entrada_departamento = Entry(janela)

    bt = Button(janela, width=10, text="Confirmar", command= bt_click)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)

    entrada_nome.grid(row=0, column=1)
    entrada_cpf.grid(row=1, column=1)
    entrada_departamento.grid(row=2, column=1)

    bt.grid(row=3,column=0, columnspan=2)

    
    janela.geometry("")
    janela.mainloop()

def janela_deletar_professor():

    def bt_click():

        cpf = entrada_cpf.get()
        professor.set_cpf(cpf)

        if not professor.apagar():
            lb2= Label(janela, text="Professor apagado")
            lb2.grid(row=2 ,column=0, columnspan=2)
        else:
            lb3= Label(janela, text="Professor não existente")
            lb3.grid(row=2 ,column=0, columnspan=2)
        

    janela = Tk()
    
    lb1 = Label(janela, text="Digite o CPF: ")
    
    entrada_cpf = Entry(janela)
    

    bt = Button(janela, width=10, text="Confirmar", command= bt_click)

    lb1.grid(row=0, column=0)
    
    entrada_cpf.grid(row=0, column=1)
   
    bt.grid(row=1,column=0, columnspan=2)

    
    janela.geometry("")
    janela.mainloop()


def janela_atualizar_professor():

    def bt_click():

        cpf = entrada_cpf.get()
        novo_nome = entrada_novo_nome.get()
        novo_cpf = entrada_novo_cpf.get()
        novo_departamento = entrada_novo_departamento.get()

        professor.set_cpf(cpf)

        if not professor.atualizar(novo_nome, novo_cpf, novo_departamento):
            lb5 = Label(janela, text="Professor atualizado")
            lb5.grid(row=5, column=0, columnspan=2)
        else:
            lb6 = Label(janela, text="Professor Não existente")
            lb6.grid(row=5, column=0, columnspan=2)

    janela = Tk()
    
    lb1 = Label(janela, text="Digite o CPF: ")
    lb2 = Label(janela, text="Digite o novo Nome: ")
    lb3 = Label(janela, text="Digite o novo Cpf: ")
    lb4 = Label(janela, text= "Digite o novo Departamento: ")

    entrada_cpf = Entry(janela)
    entrada_novo_nome = Entry(janela)
    entrada_novo_cpf = Entry(janela)
    entrada_novo_departamento = Entry(janela)

    bt = Button(janela, width= 10, text="confirmar", command= bt_click)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    lb4.grid(row=3, column=0)
    
    entrada_cpf.grid(row=0, column=1)
    entrada_novo_nome.grid(row=1, column=1)
    entrada_novo_cpf.grid(row=2, column= 1)
    entrada_novo_departamento.grid(row=3, column=1)


    bt.grid(row=4, column=0, columnspan=2)
    
    janela.geometry("")
    janela.mainloop()


def disciplinas_menu():
    
    janela_alunos = Tk()

    lb1 = Label(janela_alunos, text="--- SISTEMA ACADEMICO / Disciplinas ---")
    lb2 = Label(janela_alunos, text="===============================================")
    lb3 = Label(janela_alunos, text="--- Escolha uma opção ---")
    lb4 = Label(janela_alunos, text="===============================================")
    
    bt1 = Button(janela_alunos, width= 20, text="Listar")
    bt2 = Button(janela_alunos, width= 20, text="Adicionar", command= janela_adicionar_disciplina)
    bt3 = Button(janela_alunos, width= 20, text="Deletar", command= janela_deletar_disciplina)
    bt4 = Button(janela_alunos, width= 20, text="Atualizar", command= janela_atualizar_disciplina)
  
    lb5 = Label(janela_alunos, text="==============================================")

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    lb4.grid(row=3, column=0)

    bt1.grid(row=4,column=0)
    bt2.grid(row=5,column=0)
    bt3.grid(row=6,column=0)
    bt4.grid(row=7,column=0)

    lb5.grid(row=9,column=0)

    janela_alunos.geometry("")
    janela_alunos.mainloop()

def janela_adicionar_disciplina():

    def bt_click():
        nome = entrada_nome.get()
        codigo = entrada_codigo.get()
        disciplina.set_nome(nome)
        disciplina.set_codigo(codigo)

        if not disciplina.adicionar():
            lb3 = Label(janela, text="Disciplina adicionada")
            lb3.grid(row=3, column=0,columnspan=2)
        else:
            lb4 = Label(janela, text="Disciplina já esixtente")
            lb4.grid(row=3, column=0,columnspan=2)


    janela = Tk()
    
    lb1 = Label(janela, text="Digite o Nome: ")
    lb2 = Label(janela, text="Digite o Codigo: ")

    entrada_nome = Entry(janela)
    entrada_codigo = Entry(janela)

    bt = Button(janela, width= 10, text="confirmar", command= bt_click)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    
    entrada_nome.grid(row=0, column=1)
    entrada_codigo.grid(row=1, column=1)

    bt.grid(row=2, column=0, columnspan=2)
    
    janela.geometry("")
    janela.mainloop()

def janela_deletar_disciplina():

    def bt_click():
        codigo = entrada_codigo.get()
        disciplina.set_codigo(codigo)

        if  not disciplina.apagar():
            lb2 = Label(janela, text="Disciplina Apagada")
            lb2.grid(row=2, column=0, columnspan=2)
        else:
            lb3 = Label(janela, text="Disciplina não existente")
            lb3.grid(row=2, column=0, columnspan=2)
    
    janela = Tk()
    
    lb1 = Label(janela, text="Digite o Codigo: ")

    entrada_codigo = Entry(janela)

    bt = Button(janela, width= 10, text="confirmar", command= bt_click)

    lb1.grid(row=0, column=0)

    entrada_codigo.grid(row=0, column=1)

    bt.grid(row=1, column=0, columnspan=2)
    
    janela.geometry("")
    janela.mainloop()

def janela_atualizar_disciplina():

    def bt_click():
        
        codigo = entrada_codigo.get()
        novo_nome = entrada_novo_nome.get()
        novo_codigo = entrada_novo_codigo.get()

        disciplina.set_codigo(codigo)

        if not disciplina.atualizar(novo_nome, novo_codigo):
            lb4 = Label(janela, text="Disciplina atualizada")
            lb4.grid(row=4, column=0, columnspan=2)
        else:
            lb5 = Label(janela, text="Disciplina não existente")
            lb5.grid(row=4, column=0, columnspan=2)
    
    janela = Tk()
    
    lb1 = Label(janela, text="Digite o Codigo: ")
    lb2 = Label(janela, text="Digite o novo Nome: ")
    lb3 = Label(janela, text="Digite o novo Codigo: ") 

    entrada_codigo = Entry(janela)
    entrada_novo_nome = Entry(janela)
    entrada_novo_codigo = Entry(janela)

    bt = Button(janela, width= 10, text="confirmar", command= bt_click)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    
    entrada_codigo.grid(row=0, column=1)
    entrada_novo_nome.grid(row=1, column=1)
    entrada_novo_codigo.grid(row=2, column= 1)

    bt.grid(row=3, column=0, columnspan=2)
    
    janela.geometry("")
    janela.mainloop()







