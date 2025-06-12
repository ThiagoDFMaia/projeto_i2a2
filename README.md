# Desafio 2 – Agentes de Inteligência Artificial (i2a2)

Este projeto foi desenvolvido como parte do **Desafio 2** do curso da plataforma [i2a2](https://i2a2.com.br), com foco na criação de agentes de inteligência artificial.

## Objetivo

Criar um sistema com **agentes de IA** capazes de descompactar arquivos  e responder, de forma inteligente, às perguntas dos usuários referente aos arquivos descompactados.

## Estrutura do Projeto

O projeto está dividido em quatro agentes principais:

### 1. Agente de Prompt

Responsável por:

- Receber a pergunta do usuário
- Selecionar uma amostra dos dados
- Gerar um prompt estruturado com o passo a passo necessário para encontrar a resposta

### 2. Agente descompactador

Responsável por:

- Receber o arquivo compactado
- Descompacta os arquivos
- Retorna o dataset dos arquivos agrupados.

### 3. Agente Programador

Responsável por:

- Gera o melhor codigo python para responder a pergunta do usuário
- Gera o código para agrupar os arquivos
- Retorna o código para ser executado
- Gera gráficos

### 4. Agente executor

Responsável por:

- Cria a classe agente
- Envia os comandos para os outros agentes
- Guarda os dados do dataset e chaves

## Interface

No momento, a interface é baseada em terminal (console).  
O próximo passo será desenvolver uma interface web com **Flask**, tornando o sistema mais acessível e amigável ao usuário final.

## Estrutura de Arquivos

├── dataset/
│ ├── 202401_NFs_Cabecalho.csv
│ └── 202401_NFs_Itens.csv
├── agente.py
├── requirements.txt
└── README.md


## Como Executar

1. Clone o repositório:

* git clone https://github.com/ThiagoDFMaia/projeto_i2a2.git


2. Instale as dependências:
* pip install -r requirements.txt

3. Execute o projeto:
* python agente.py

## Próximos Passos
* Criar uma interface web com Flask

* Permitir upload de arquivos CSV pelo usuário

* Tornar os agentes independentes e reutilizáveis

* Armazenar logs das perguntas e respostas

* Permitir o uso de outros modelos de LLMS

## Contribuição
* Contribuições são bem-vindas!
* Sinta-se à vontade para abrir issues ou enviar pull requests.