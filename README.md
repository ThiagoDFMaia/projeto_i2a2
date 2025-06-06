# Desafio 2 – Agentes de Inteligência Artificial (i2a2)

Este projeto foi desenvolvido como parte do **Desafio 2** do curso da plataforma [i2a2](https://i2a2.com.br), com foco na criação de agentes de inteligência artificial.

## Objetivo

Criar um sistema com **agentes de IA** capazes de interpretar **dados de notas fiscais** e responder, de forma inteligente, às perguntas dos usuários.

## Estrutura do Projeto

O projeto está dividido em três agentes principais:

### 1. Agente de Prompt

Responsável por:

- Receber a pergunta do usuário
- Selecionar uma amostra dos dados
- Gerar um prompt estruturado com o passo a passo necessário para encontrar a resposta

### 2. Agente Executor

Responsável por:

- Receber o conjunto de dados completo
- Executar os passos gerados pelo Agente de Prompt
- Gerar uma resposta baseada na análise dos dados

### 3. Agente Validador

Responsável por:

- Receber a resposta gerada pelo Executor
- Validar a coerência e precisão da resposta
- Apontar possíveis erros ou inconsistências

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

## Contribuição
* Contribuições são bem-vindas!
* Sinta-se à vontade para abrir issues ou enviar pull requests.


### Dicas finais:
- Salve isso num arquivo com o nome **`README.md`** (sem acento).
- Coloque esse arquivo na raiz do repositório.
- O GitHub renderiza automaticamente em formato bonito quando você acessa a página principal do repositório.

Se quiser, posso gerar o `requirements.txt` certinho também! Deseja isso agora?
