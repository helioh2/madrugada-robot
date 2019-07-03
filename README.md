# The Madrugada Robot

This is a Logo-like educational programming environment which uses a real whiteboard to make a robot that draws on it. The pen simulates a turtle that walks around a 2D board, just like in the original Logo. The idea is to stimulate learning by means of a programmable physical robot.

The physical scheme and firmware was based on the drawing robot Makelangelo: http://www.makelangelo.com/

This project uses only open source software and hardware.

# Installing

Make sure to install Flask:
```
sudo apt-get install python3-flask
```

Install also dependencies for bluetooth usage:

```
sudo apt-get install bluetooth libbluetooth-dev
sudo python3 -m pip install pybluez
```

Then run `run.sh`. If it does not run, make sure you have permission: `chmod +x ./run.sh`.
 
