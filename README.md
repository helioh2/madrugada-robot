_Para instruções em Português, abra o arquivo README.pt_br.md_

# The Madrugada Robot

This is a Logo-like educational programming environment which uses a real whiteboard to make a robot that draws on it. The pen simulates a turtle that walks around a 2D board, just like in the original Logo. The idea is to stimulate learning by means of a programmable physical robot. A block-based programming language similar to Scratch is provided, in order to make programming more intuitive and fun.

The physical scheme and firmware was based on the drawing robot Makelangelo: http://www.makelangelo.com/

This project uses only open source software and hardware.

# Installing

## Using Docker (recommended):

In any operating systems, like Linux, Windows or Mac, make sure to have Docker installed and Docker Daemon running. Then, open a terminal / command prompt and run the following command:

```
docker-compose up
```

Then, enter http://localhost:5000 in a browser (Chrome or Firefox are suggested).

## Without Docker, on Ubuntu/Debian:

Install Python and Pipenv:
```
sudo apt-get install python python-pip
pip install pipenv
```

Install also dependencies for bluetooth usage:
```
sudo apt-get install bluetooth libbluetooth-dev
pip install pybluez
```

Then run `pipenv run flask run`. Then, enter http://localhost:5000 in a browser (Chrome or Firefox are suggested).
 
