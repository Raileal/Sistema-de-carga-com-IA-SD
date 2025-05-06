🧠 Sistema de Processamento Distribuído com RabbitMQ e IA
📝 Descrição
Sistema distribuído que implementa processamento assíncrono de imagens usando RabbitMQ como message broker.
O sistema simula:

Análise de emoções em faces

Identificação de times de futebol

🏗️ Arquitetura
Componentes:

Gerador: Produz mensagens simuladas (5+ msgs/segundo)

RabbitMQ: Message broker com topic exchange

Consumidor Face: Análise de emoções (3-5s por mensagem)

Consumidor Team: Identificação de times (4-7s por mensagem)

🚀 Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/Raileal/Sistema-de-carga-com-IA-SD  
cd Sistema-de-Carga-com-IA  
Execute com Docker Compose:

bash
Copiar
Editar
docker-compose up --build  
Acesse o RabbitMQ Management:

URL: http://localhost:15672

Usuário: guest

Senha: guest

📁 Estrutura do Projeto
bash
Copiar
Editar
trabalho06/
├── gerador_mensagens/
│   ├── app.py             # Gerador de mensagens
│   ├── Dockerfile
│   └── requirements.txt
├── consumidor_face/
│   ├── app.py             # Processamento de faces
│   ├── Dockerfile
│   └── requirements.txt
├── consumidor_team/
│   ├── app.py             # Processamento de times
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml     # Configuração dos containers
└── README.md
📊 Demonstração
1️⃣ Inicialização
Abra o terminal na pasta onde está localizado o arquivo docker-compose.yml e execute:

bash
Copiar
Editar
docker-compose up --build
Aguarde a construção dos containers e o início da exibição das mensagens.

Mensagens amarelas: IA de identificação dos times

Mensagens azuis: IA de reconhecimento facial

2️⃣ Acessando o RabbitMQ
Abra o navegador e acesse: http://localhost:15672

Usuário: guest

Senha: guest

Você verá a tela de login e, após acessar, a interface geral do RabbitMQ.

3️⃣ Monitorando as Filas
No menu, clique em "Queues e Streams".

Você verá algo como:

Filas acumulando na seção "Ready", indicando mensagens esperando processamento.

