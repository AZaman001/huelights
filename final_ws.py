#!/usr/bin/python
from flask import Flask
from flask import request
from flask import jsonify
from phue import Bridge
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

b = Bridge('192.168.1.38')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# switches lights from current status
@app.route('/opposite/')
def opposite():

    # provide lightId as a get request parameter to use a specific light. 
    lightId = request.args.get('lightId')

    if lightId == None:
    # all lights
        lights = b.get_light_objects()

        for light in lights:
            light.on = not light.on
    else:
        try:
            intLightId = int(lightId)
            b.set_light(intLightId,'on',not b.get_light(intLightId,'on'))
        except ValueError:
            b.set_light(lightId,'on',not b.get_light(lightId,'on'))
    
    return 'OK'


@app.route('/on')
def turnOn():

    # provide lightId as a get request parameter to use a specific light. 
    lightId = request.args.get('lightId')

    if lightId == None:
        # all lights
        lights = b.get_light_objects()

        for light in lights:
            light.on = True
    else:
        try:
            intLightId = int(lightId)
            b.set_light(intLightId,'on',True)
        except ValueError:
            b.set_light(lightId,'on',True)

    return 'OK'


@app.route('/off')
def turnOff():

    # provide lightId as a get request parameter to use a specific light. 
    lightId = request.args.get('lightId')

    if lightId == None:
        # all lights
        lights = b.get_light_objects()

        for light in lights:
            light.on = False
    else:
        try:
            intLightId = int(lightId)
            b.set_light(intLightId,'on',False)
        except ValueError:
            b.set_light(lightId,'on',False)

    return 'OK'


@app.route('/max')
def max():

    # provide lightId as a get request parameter to use a specific light. 
    lightId = request.args.get('lightId')

    if lightId == None:
        # all lights
        lights = b.get_light_objects()

        for light in lights:
            light.brightness = 254
    else:
        try:
            intLightId = int(lightId)
            b.set_light(intLightId,'bri',254)
        except ValueError:
            b.set_light(lightId,'bri',254)

    return 'OK'


@app.route('/dim')
def dim():

    # provide lightId as a get request parameter to use a specific light. 
    lightId = request.args.get('lightId')

    if lightId == None:
        # all lights
        lights = b.get_light_objects()

        for light in lights:
            light.brightness = 100
    else:
        try:
            intLightId = int(lightId)
            b.set_light(intLightId,'bri',100)
        except ValueError:
            b.set_light(lightId,'bri',100)

    return 'OK'

@app.route('/status')
def status():

    light_list = []

    # provide lightId as a get request parameter to get a specific light. 
    lightId = request.args.get('lightId')

    if lightId == None:
        # all lights
        lights = b.get_light_objects()

        for light in lights:
            light_status = {
            'id':light.light_id,
            'name':light.name,
            'on':light.on,
            'brightness':light.brightness
            }
            light_list.append(light_status)
    else:
        try:
            intLightId = int(lightId)
            light_status = {
            'id':b[intLightId].light_id,
            'name':b[intLightId].name,
            'on':b[intLightId].on,
            'brightness':b[intLightId].brightness
            }
            light_list.append(light_status)
        except ValueError:
            intLightId = int(lightId)
            light_status = {
            'id':b[lightId].light_id,
            'name':b[lightId].name,
            'on':b[lightId].on,
            'brightness':b[lightId].brightness
            }
            light_list.append(light_status)
    return jsonify({'light_list':light_list})

@app.route('/random_color')
def random_color():

    # provide lightId as a get request parameter to use a specific light. 
    lightId = request.args.get('lightId')

    if lightId == None:
        # all lights
        lights = b.get_light_objects()

        for light in lights:
            light.xy = [random.random(),random.random()]
    else:
        try:
            intLightId = int(lightId)
            b.set_light(intLightId,'xy',[random.random(),random.random()])
        except ValueError:
            b.set_light(lightId,'xy',[random.random(),random.random()])

    return 'OK'


# Cozmo program to go 'get towels'
def cozmo_program(robot: cozmo.robot.Robot):

	# uncomment if you want Cozmo to say that he is getting towels
	#robot.say_text(f"I am going to go get towels").wait_for_completed()

    # reset Cozmo's arms and head
    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

    robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()


@app.route('/go')
def cozmo_go():

	# make Cozmo "go" [get towels] or something as the end point is hit
    cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
    return 'OK'








