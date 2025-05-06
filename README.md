Para rodar o projeto, siga os seguintes passos:

1° Para criar a estrutura do projeto, vá até o diretório onde o arquivo docker-compose.yaml está localizado, usando o terminal. Em seguida, execute o comando docker-compose up --build, que criará a estrutura do projeto.

2° Após isso, aguarde até que o processo de construção seja concluído e comecem a aparecer as mensagens referentes às IAs: a azul, que representa a IA de identificação dos times, e a vermelha, que representa a IA de reconhecimento de expressão facial.
![Captura de tela 2025-05-05 215242](https://github.com/user-attachments/assets/d9f657f0-d0ce-45e5-b527-db838be029ed)

3° Com o progama em execução, abra o navegador e bote o seguinte link: http://localhost:15672. O link abrirá o site do rabbit no qual ele pedirá uma senha e login.
![Captura de tela 2025-05-05 215540](https://github.com/user-attachments/assets/db140a46-2d52-451c-bc22-9defa064ab7a)
Para esta etapa usa "guest" para autenticar no login e senha.

4° após isto abrirá o menu geral que mostrará a seguinte imagem.
![image](https://github.com/user-attachments/assets/91c367f5-7e84-4c0e-930a-f8db4bf2d89f)
Para ver a fila de processamento em crescimento aperte na opção de "Queues e Streams" e você verá a seguinte tela:
![image](https://github.com/user-attachments/assets/70a87819-f8f6-4acc-ac34-a96d19550aed)
Na tela em questão será possível ver a fila acumulando na categoria ready.
