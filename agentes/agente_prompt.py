from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def gerar_prompt(pergunta,historico,chave,df):
    dados_texto = df.head(10).to_string(index=False)

    historico_texto = ""
    if historico:
    
        historico_texto += "CONTEXTO DE CONVERSA ANTERIOR:\n"
        
        # Itera sobre cada dicionário no histórico
        for mensagem in historico:
            
            # Extrai a pergunta e a resposta usando suas chaves
            p = mensagem.get("pergunta", "N/D") 
            r = mensagem.get("resposta", "N/D")

            # Adiciona a pergunta e a resposta no formato desejado
            historico_texto += f"USUÁRIO: {p}\n"
            historico_texto += f"ASSISTENTE: {r}\n"
            
        historico_texto += "--- FIM DO CONTEXTO ANTERIOR ---\n\n"


    prompt_template = PromptTemplate(
        input_variables=["dados"],
        template="""
        Você é um engenheiro de prompt.

        Vai receber algumas linhas de um conjunto de dados e vai tentar responder a pergunta do usuario.
        Você não vai criar nenhum codigo.

        

        Aqui esta o conjunto de dados:

        {dados}


        Pergunta:

        {pergunta}

        Responda **apenas em JSON válido**, sem explicações, sem ```
        
        - Se a pergunta puder ser respondida só com texto, responda com json nesse formato:
           - {{"tipo": "texto", "conteudo": "<sua resposta>"}}

        - Se precisar gerar código, responda com json nesse formato:
            - {{"tipo": "codigo", "conteudo": "<prompt que descreve como gerar o código>"}}
            - Importante:
            - Vai só criar o melhor prompt para responder a pergunta.
            - O prompt vai ser enviado para um agente programador python para fazer um codigo python.
            - O agente programador deve ser capaz de elabora um codigo com o prompt que voce descreveu para responder a pergunta.
            - O código gerado tem que estar necessariamente em python.
            - A variável com o dataset está obrigatoriamente em 'df_total'
        
        - Se precisar gerar um gráfica, responda com json nesse formato:
            - {{"tipo": "grafico", "conteudo": "<prompt que descreve como gerar o grafico>"}}
            - Importante:
            - Vai só criar o melhor prompt para gerar o grafico.
            - O prompt vai ser enviado para um agente programador python para fazer um codigo python.
            - O agente programador deve ser capaz de elabora um gráfico com o prompt que voce descreveu para responder a pergunta.
            - O código gerado tem que estar necessariamente em python.
            - A variável com o dataset está obrigatoriamente em 'df_total'
            - o gráfico gerado tem que usar obrigatoriamente o matplotlib.pyplot as plt
            - não vai mostrar o grafico, o grafico tem que ficar obrigatoriamente na variável 'fig' em 'fig, ax = plt.subplots()'
            - Obrigatoriamente Não chame plt.show()
              - **Obrigatoriamente, não use fig.canvas.draw() nem converta a figura para bytes (por exemplo, fig.canvas.tostring_png())**
              - 'fig' tem que obrigatoriamente ser plotada no streamliT depois. NÃO AGORA!
        * IMPORTANTE:
            - Para calculos SEMPRE vá no tipo "codigo"


        * Aqui o historico das perguntas do usuario:
        {hist}

        """
        )
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=chave)

    chain = prompt_template | llm
    resposta = chain.invoke({"dados": dados_texto, "pergunta": pergunta,"hist":historico_texto})
  

    return resposta.content