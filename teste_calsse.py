from Aluno import Aluno
import sqlite3

daniel = Aluno()
daniel.set_nome(input("Digite o nome: "))
daniel.set_cpf(input("Digite cpf: "))

daniel.adicionar_ao_banco()

daniel.listar_todos()




