import random 
alunos = ["João", "Maria", "Pedro", "Ana", "Lucas", "Mariana"]
#embaralha a lista
random.shuffle(alunos)
print(f"Lista embaralhada aleatoriamente {alunos}")
#escolha um aluno aleatoriamente
sorteada = random.choice(alunos)
print(f"Aluno sorteado: {sorteada}")