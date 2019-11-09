#!/usr/bin/python
from flask import Flask
from phue import Bridge

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello, World!"

b = Bridge('192.168.1.38')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()


@app.route('/opposite')
def opposite():

    # Prints if light 1 is on or not
    isOn = b.get_light(2, 'on')
    #print(isOn)

    if (isOn == True): 
        # Turn lamp 2 on
        b.set_light(2,'on', False)
    else:
        b.set_light(2,'on', True)
    
    return 'OK'


@app.route('/on')
def turnOn():
    b.set_light(2,'on', True)

    return 'OK'


@app.route('/off')
def turnOff():
    b.set_light(2,'on', False)

    return 'OK'


@app.route('/max')
def max():
    b.set_light(2, 'bri', 254)

    return 'OK'

@app.route('/dim')
def dim():
    b.set_light(2, 'bri', 100)

    return 'OK'