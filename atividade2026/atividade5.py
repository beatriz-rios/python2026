alunos =["Michele OLiveira"]
alunos.append("João Silva")
while True:
    nome = input ("Digite o nome do aluno:")
    alunos.append(nome)
    resposta = input ("Deseja adicionar mais um aluno? (s/n)")
    if resposta.upper() == "n":
        break
print(f"Alunos cadastrados: {alunos}")