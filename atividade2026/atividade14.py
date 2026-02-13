agentes = {"007": "Londres",
    "Viúva Negra": "Budapeste",
    "Etham Hunt": "Paris"} 


nome_agente = input("Digite o nome do agente: ")
if agentes.get(nome_agente) is None:
        print("Agente Desconhecido.")
elif nome_agente in agentes:
        print(f"O agente {nome_agente} está em {agentes[nome_agente]}.")
    
agentes.update({"007":"Canadá"})
agentes.update({"Trinity": "Matrix"})
#relatorio geral
relatorio = input("Deseja ver o relatório geral? (s/n): ")
if relatorio.lower() == "s":
    print("Relatório geral Atualizado:")
    for agente, local in agentes.items():
        print(f"O agente {agentes} está em {local}")