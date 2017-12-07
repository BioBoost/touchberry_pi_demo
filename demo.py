from time import sleep
import sys
from touchberrypi import TouchberryPi
from touchberrypi import Color
from touchberrypi import Colors
from touchberrypi import Led
from touchberrypi import TouchKey
from simplemqttclient import SimpleMqttClient

def message_handler(client, userdata, msg):
    print("Received: " + msg.payload.decode('utf-8'))

mqttClient = SimpleMqttClient("shazooble")
mqttClient.subscribe("bioboost/sensors/temp", message_handler)

shield = TouchberryPi()
shield.set_all_leds(Colors.RED)

def on_key_up(key):
    print("Key {} released".format(key))
    if key == TouchKey.UP:
        shield.set_led(Led.LED1, Colors.RED)
    elif key == TouchKey.DOWN:
        shield.set_led(Led.LED2, Colors.RED)
    elif key == TouchKey.LEFT:
        shield.set_led(Led.LED3, Colors.RED)
    elif key == TouchKey.RIGHT:
        shield.set_led(Led.LED4, Colors.RED)
    elif key == TouchKey.X:
        shield.set_led(Led.LED5, Colors.RED)

def on_key_down(key):
    print("Key {} pressed".format(key))
    if key == TouchKey.UP:
        shield.set_led(Led.LED1, Colors.GREEN)
    elif key == TouchKey.DOWN:
        shield.set_led(Led.LED2, Colors.GREEN)
    elif key == TouchKey.LEFT:
        shield.set_led(Led.LED3, Colors.GREEN)
    elif key == TouchKey.RIGHT:
        shield.set_led(Led.LED4, Colors.GREEN)
    elif key == TouchKey.X:
        shield.set_led(Led.LED5, Colors.GREEN)

def on_key_change(key, state):
    print("Key {} changed state to {}".format(key, state))

shield.on_key_up(on_key_up)
shield.on_key_down(on_key_down)
shield.on_key_change(on_key_change)

shield.start_touch_listener(0.1)
mqttClient.start()

try:
    while True:
        temp = shield.temperature()
        print("Temperature = " + str(temp))
        mqttClient.publish("bioboost/shield/temperature", str(temp))
        sleep(5)
except KeyboardInterrupt:       # Catch CTRL-C
    mqttClient.stop()
    print ("Bye Bye")
    sys.exit()
