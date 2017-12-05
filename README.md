# python-touchberrypi
Python library for the Touchberry Pi shield for the Raspberry Pi

# Python 3

As default we need python 3 so:

```shell
sudo apt-get install python3
```

## Install SmBus python package

```shell
sudo apt-get update && sudo apt-get install python3-smbus
```

## Some info on SmBus methods

[http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2](http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2)

## Extras

Per Debian policy, python refers to Python 2 and python3 refers to Python 3. Don't try to change this system-wide or you are in for trouble.

List installed python packages:

```shell
pip3 freeze
```
