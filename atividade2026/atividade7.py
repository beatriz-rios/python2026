import random
alunos = ["João", "Maria", "Pedro", "Ana", "Lucas", "Mariana"]
#embaralha a lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
#ordena a lista crescente
alunos.sort()
print(f"Lista ordenada aleatoriamente: {alunos}")
#ordena a lista decrescente
alunos.sort(reverse=True)
print(f"Lista ordenada decrescente: {alunos}")