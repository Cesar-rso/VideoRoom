# VideoRoom
Salas de compartilhamento de video

Projeto em Django. Necessário ter python 3.10 instalado.

# Como executar
 1 - Docker: Com o prompt de comando (ou Terminal, caso seja Linux) na pasta principal do projeto (onde se encontra o Dockerfile) execute o comando: 
 docker build -t videoroom ./
Esse comando irá criar a imagem Docker. Se executar a imagem no Docker desktop, ligue a porta Container tcp 80 à porta 8000. Se executar pelo prompt, 
execute o comando: docker run -p 80:8000 videoroom
Agora basta abrir o browser no endereço localhost:8000

2 - Localhost: Para executar na máquina local, Com o prompt de comando (ou Terminal, caso seja Linux) na pasta principal do projeto (onde se encontra o 
arquivo requirements.txt) execute o comando: pip install --no-cache-dir -r requirements.txt
Esse comando irá instalar todas as dependencias. A seguir, execute o comando: gunicorn --bind=0.0.0.0:8000 --workers=2 VideoRoom.wsgi
Agora basta abrir o browser no endereço 0.0.0.0:8000
