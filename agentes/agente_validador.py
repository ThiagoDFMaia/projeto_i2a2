from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def validar_resultado(resposta,chave,prompt):
   
    prompt_template = PromptTemplate(
        input_variables=["resposta"],
        template="""
        Você é um agente validador.

        Vai receber a resposta de um prompt e o prompt que foi realizado.
        Vai validar a resposta.
       
        Se a resposta estiver correta voce retorna somente o resultado final de tudo.
        Se estiver errado retorna o resultado que encontrou.
      
    
    

        Aqui esta a resposta:
        {resposta}

        prompt:
        {prompt}
        """
        )
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=chave)

    chain = prompt_template | llm
    resposta = chain.invoke({"resposta": resposta, "prompt": prompt})
  

    return resposta.content