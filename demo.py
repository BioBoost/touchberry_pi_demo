from touchberrypi import TouchberryPi

# def on_key_up(key):
#     print("Key {} pressed".format(key))
#
#
# touchberrypi.attach(on_key_up)
#
# print(touchberrypi.get_temperature())
#
# touchberrypi.set_all_leds("blue")
#
# touchberrypi.set_led(5, "red")


shield = TouchberryPi()

print("Temperature = " + str(shield.get_temperature()))

def key_change_handler(key, state):
    print("Key {} changed state to {}".format(key, state))

shield.on_key_change(key_change_handler)

print("Touch chip id = " + str(shield.get_touch().chip_id()))
