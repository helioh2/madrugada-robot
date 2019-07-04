# O Robô Madrugada

Este é um ambiente educacional de programação estilo Logo, que utiliza uma lousa de verdade para fazer um robô que desenha na lousa. A caneta simula uma tartaruga que anda sobre uma plataforma bidimensional, assim como o sistema Logo original. A ideia é estimular o aprendixado por meio de um robô fisicamente programável. A programação é realizada por meio de uma linguagem de programação em blocos, semelhante ao Scratch, de modo a tornar a aprendizagem mais intuitiva e lúdica.

O projeto físico e a firmware são baseados no robô desenhador de lousa Makelangelo: http://www.makelangelo.com/


# Instalação

## Usando Docker (recomendado):

Em qualquer sistema, seja Linux, Windows ou Max, certifique-se de ter instalado o Docker e de que o Docker Daemon está em execução. Então, abra um terminal / prompt de comando e execute o seguinte comando:

```
docker-compose up
```

Basta entrar, então, em http://localhost:5000 em um navegador (recomenda-se Chrome ou Firefox)

_Para instalação do Docker no Windows: https://docs.docker.com/docker-for-windows/install/ _

## Sem Docker, em um sistema Ubuntu/Debian:

Instale o Python e o Pipenv:
```
sudo apt-get install python python-pip
pip install pipenv
```

Instale também as dependências para o uso do bluetooth:
```
sudo apt-get install bluetooth libbluetooth-dev
pip install pybluez
```

Então execute o comando `pipenv run flask run`. Depois, entre no endereço http://localhost:5000 em um navegador (recomenda-se Chrome ou Firefox)
 