from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def executar_prompt(pergunta,chave,df,prompt):
    dados_texto = df.to_string(index=False)
    prompt_template = PromptTemplate(
        input_variables=["dados"],
        template="""
        Você é um agente executor.

        Vai receber um prompt e um conjunto de dados para responder a pergunta.
        Não é para retornar codigo de programação.

        Vai executar passo a passo o que foi ordenado no prompt.
      
        E retornar o resultado do comando e descrever o que voce fez.
    

        Aqui esta o conjunto de dados:
        {dados}

        prompt:
        {prompt}

        Pergunta:
        {pergunta}
        """
        )
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=chave)

    chain = prompt_template | llm
    resposta = chain.invoke({"dados": dados_texto, "pergunta": pergunta,"prompt": prompt})
  

    return resposta.content