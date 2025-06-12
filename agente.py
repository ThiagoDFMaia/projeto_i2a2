

import pandas as pd
import matplotlib as mlt
from agentes import  agente_executor as executor


chave='coloque aqui sua chave do gemini studio'
url='endereco do arquivo compactado'
agente=executor.Agente()
agente.carrega_arquivos(url=url, chave=chave)
agente.df.info()




# 🔄 Loop interativo para perguntas
while True:
    pergunta = input("Digite sua pergunta ou dados (ou 'sair' para encerrar): ")
    if pergunta.strip().lower() in ["sair", "exit", "quit"]:
        print("👋 Encerrando o agente.")
        break
   

    agente.pergunta(pergunta)
    
 