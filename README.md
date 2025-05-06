Para rodar o projeto siga os seguintes passos:

1° para a criação da estrutura do projeto é preciso apenas ir no diretorio onde o arquivo docker-compose-yaml esta presente pelo terminal, apos isto execute o comando 
"docker-compose up --build", no qual ele criará a estrutura do projeto.

2° Após isto espere ate que ele termine de contruir e que começe a aparecer as mensagens referentes as IAs, no caso a azul sendo a IA que representa a indentificação dos 
times e a azul a do reconhecimento da expressão facial.
![Captura de tela 2025-05-05 215242](https://github.com/user-attachments/assets/d9f657f0-d0ce-45e5-b527-db838be029ed)

3° Com o progama em execução, abra o navegador e bote o seguinte link: http://localhost:15672. O link abrirá o site do rabbit no qual ele pedirá uma senha e login.
![Captura de tela 2025-05-05 215540](https://github.com/user-attachments/assets/db140a46-2d52-451c-bc22-9defa064ab7a)
Para esta etapa usa "guest" para autenticar no login e senha.

4° após isto abrirá o menu geral que mostrará a seguinte imagem.
![image](https://github.com/user-attachments/assets/91c367f5-7e84-4c0e-930a-f8db4bf2d89f)
Para ver a fila de processamento em crescimento aperte na opção de "Queues e Streams" e você verá a seguinte tela:
![image](https://github.com/user-attachments/assets/70a87819-f8f6-4acc-ac34-a96d19550aed)
Na tela em questão será possível ver a fila acumulando na categoria ready.
