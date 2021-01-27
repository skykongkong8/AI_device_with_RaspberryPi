import RPi.GPIO as g
from time import sleep
from ears_universal import listen
from mouth import talk

g.setmode(g.BCM)
sensor = 26

g.setup(26, g.IN)
print('Press ctrl+C to quit')

try:
    while True:
        value = g.input(26)
        if value == True:
            print('sensor detected')
            what_said = listen()
            talk(what_said)
        else:
            #print('no detection')
            pass
except KeyboardInterrupt:
    g.cleanup()
    print('Goodbye.')

