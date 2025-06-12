import os
import io
import pandas as pd
from agentes import agente_prompt as prompt,agente_programador as programador, agente_descompactador as descompactador, agente_validador as validador


class Agente:
    def __init__(self):
        self.url=''
        self.chave=''
        self.df=None

    def carrega_arquivos(self,url, chave):

        # 👉 Coloque sua chave da API Gemini aqui:
        os.environ["GOOGLE_API_KEY"] = chave


        arquivos=descompactador.descompactar_arquivos(url)


        amostras=descompactador.preparar_amostras_para_agente(arquivos)

        rest=programador.agrupar_arquivos(os.environ["GOOGLE_API_KEY"],amostras)
        codigo_limpo = rest.strip("```").replace("python", "").strip()

        exec_globals = {"pd": pd}
        exec_locals = {"lista_df": arquivos} # Passa 'lista_df' com os DataFrames completos
        exec(codigo_limpo, exec_globals, exec_locals)
        self.df = exec_locals.get("df")
       


    def pergunta(self,pergunta):
            prompt_gerado=prompt.gerar_prompt(pergunta,os.environ["GOOGLE_API_KEY"],self.df)
            print(prompt_gerado)
            resposta=programador.gerar_codigo(os.environ["GOOGLE_API_KEY"],self.df,prompt_gerado)
            print(resposta)
            codigo_limpo = resposta.strip("```").replace("python", "").strip()
            exec(codigo_limpo, {"df_total": self.df})
    
 