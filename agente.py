import os
import pandas as pd
from agentes import agente_prompt as prompt, agente_executor as executor, agente_validador as validador


# 👉 Coloque sua chave da API Gemini aqui:
os.environ["GOOGLE_API_KEY"] = "digite aqui sua chave do gemini"

# 🧠 Carrega os arquivos CSV
df1 = pd.read_csv("dataset/202401_NFs_Cabecalho.csv")
df2 = pd.read_csv("dataset/202401_NFs_Itens.csv")

# 🧩 Junta os dois em um único DataFrame
df_total = pd.concat([df1, df2], ignore_index=True)





# 🔄 Loop interativo para perguntas
while True:
    pergunta = input("Digite sua pergunta ou dados (ou 'sair' para encerrar): ")
    if pergunta.strip().lower() in ["sair", "exit", "quit"]:
        print("👋 Encerrando o agente.")
        break
    prompt_gerado=prompt.gerar_prompt(pergunta,os.environ["GOOGLE_API_KEY"],df_total)
    # resposta = chain.invoke({"dados": dados_texto, "pergunta": pergunta})
    print("📌Resposta prompt: ################################## \n", prompt_gerado)
    resposta=executor.executar_prompt(pergunta,os.environ["GOOGLE_API_KEY"],df_total,prompt_gerado)
    print("📌 Resposta executor: ############################### \n", resposta)
    
    resposta_validada=validador.validar_resultado(resposta,os.environ["GOOGLE_API_KEY"],prompt_gerado)
    print("📌 Resposta validador: ############################### \n", resposta_validada)
