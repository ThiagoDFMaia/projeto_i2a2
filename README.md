🧠 Desafio 2 – Agentes de Inteligência Artificial (i2a2)
Este projeto foi desenvolvido como parte do Desafio 2 do curso da plataforma i2a2, com foco na criação de agentes de inteligência artificial.

🎯 Objetivo
Criar um sistema com agentes de IA capazes de interpretar dados de notas fiscais e responder, de forma inteligente, às perguntas dos usuários.

🧩 Estrutura do Projeto
O projeto está dividido em três agentes principais:

1. 🧠 Agente de Prompt
Responsável por:

Receber a pergunta do usuário

Selecionar uma amostra dos dados

Gerar um prompt estruturado com o passo a passo necessário para encontrar a resposta

2. ⚙️ Agente Executor
Responsável por:

Receber o conjunto de dados completo

Executar os passos gerados pelo Agente de Prompt

Gerar uma resposta baseada na análise dos dados

3. ✅ Agente Validador
Responsável por:

Receber a resposta gerada pelo Executor

Validar a coerência e precisão da resposta

Apontar possíveis erros ou inconsistências

🖥️ Interface
No momento, a interface é console-based (terminal).
O próximo passo será desenvolver uma interface web com Flask, permitindo uma experiência mais amigável para o usuário final.

📂 Estrutura de Arquivos
css
Copiar
Editar
.
├── dataset/
│   ├── 202401_NFs_Cabecalho.csv
│   └── 202401_NFs_Itens.csv
├── main.py
├── requirements.txt
└── README.md
▶️ Como Executar
Clone o repositório:

bash
Instale as dependências:

bash
pip install -r requirements.txt
Execute o projeto:

bash
python agente.py

🔮 Próximos Passos
 Criar uma interface web com Flask

 Permitir upload de arquivos CSV pelo usuário

 Tornar os agentes independentes e reutilizáveis

 Armazenar logs das perguntas e respostas

🤝 Contribuição
Contribuições são bem-vindas! Fique à vontade para abrir issues ou enviar pull requests.
