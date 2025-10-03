import os
import io
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import numpy as np
# from agentes import agente_prompt as prompt,agente_programador as programador, agente_descompactador as descompactador, agente_validador as validador
from agentes import agente_prompt as prompt
from agentes import agente_programador as programador
from agentes import agente_descompactador as descompactador
from agentes import agente_descompactador_url as descompactador_url
from agentes import agente_processador_upload as processador_upload
import json
import traceback
class Agente:
    def __init__(self):
        self.chave=''
        self.df=None

    def carrega_arquivos(self, chave, url=None, arquivos_carregados=None):
        # 👉 Coloque sua chave da API Gemini aqui:
        os.environ["GOOGLE_API_KEY"] = chave

        arquivos = []
        if url: 
            print(f"Iniciando download da URL: {url}")
            arquivos=descompactador_url.descompactar_arquivos(url)
        elif arquivos_carregados:
            print(f"Iniciando processamento de arquivos carregados.")
            arquivos = arquivos = processador_upload.processar_arquivo_upload(arquivos_carregados)

        if not arquivos:
            raise ValueError("Nenhum arquivo CSV válido foi encontrado. Verifique a fonte dos dados e tente novamente.")
        
       
        if len(arquivos) == 1:
            print("📂 Apenas 1 arquivo encontrado, carregando diretamente.")
            self.df = arquivos[0]
        else:
            amostras=descompactador_url.preparar_amostras_para_agente(arquivos)
            
            rest=programador.agrupar_arquivos(os.environ["GOOGLE_API_KEY"],amostras)
            codigo_limpo = rest.strip("```").replace("python", "").strip()

            exec_globals = {"pd": pd}
            exec_locals = {"lista_df": arquivos} # Passa 'lista_df' com os DataFrames completos
            exec(codigo_limpo, exec_globals, exec_locals)
            self.df = exec_locals.get("df")

    def pergunta(self,pergunta,historico):
            try:
                fig=None
                prompt_gerado=prompt.gerar_prompt(pergunta,historico,os.environ["GOOGLE_API_KEY"],self.df)

          
                prompt_gerado = prompt_gerado.strip("```").replace("json", "").strip()
       
                #print ("promt:",prompt_gerado)
                prompt_gerado = json.loads(prompt_gerado)
             
       
                if prompt_gerado["tipo"] == "texto":
                    print("Resposta:", prompt_gerado["conteudo"])
                elif prompt_gerado["tipo"] == "codigo":
                    resposta=programador.gerar_codigo(os.environ["GOOGLE_API_KEY"],self.df,prompt_gerado["conteudo"])
              
                    codigo_limpo = resposta.strip("```").replace("python", "").strip()
                  
              
                    exec_globals = {"df_total": self.df, "plt": plt, "sns": sns}
                    exec_locals = {}
                    exec(codigo_limpo, exec_globals,exec_locals)
                elif prompt_gerado["tipo"] == "grafico":
                   
                    resposta=programador.gerar_codigo(os.environ["GOOGLE_API_KEY"],self.df,prompt_gerado["conteudo"])
              
                    codigo_limpo = resposta.strip("```").replace("python", "").strip()
                    #print ("codigo: ",codigo_limpo)
              
                    exec_globals = {"df_total": self.df, "plt": plt, "sns": sns, "pd": pd} 

                    exec_locals = {}
                    exec(codigo_limpo, exec_globals,exec_locals)
                    fig = exec_locals.get("fig") or exec_globals.get("fig")

              
                    #plt.close(fig) 
    
                    
                    return fig    
         
            except Exception as e:                           
                traceback.print_exc()
                print("Erro ao interpretar resposta, mostrando bruto:", e)
          