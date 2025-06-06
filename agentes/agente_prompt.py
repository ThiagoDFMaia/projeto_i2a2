from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def gerar_prompt(pergunta,chave,df):
    dados_texto = df.head(10).to_string(index=False)
    prompt_template = PromptTemplate(
        input_variables=["dados"],
        template="""
        Você é um engenheiro de prompt.

        Vai receber algumas linhas de um conjunto de dados e fazer o melhor prompt para responder a pergunta do usuario.

        O prompt pode descrecrever detalhadamente o passo a passo para responder a pergunta.
        Não vai retornar os dados.
        Não vai retornar codigo de programação.
        

        Aqui esta o conjunto de dados:

        {dados}


        Pergunta:

        {pergunta}
        """
        )
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=chave)

    chain = prompt_template | llm
    resposta = chain.invoke({"dados": dados_texto, "pergunta": pergunta})
  

    return resposta.content