import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)

def get_last_watered():
    try:
        f=open('last_watered.txt',"r")
        return f.readline()
        f.close()
    except:
        return "NEVER!"

def get_status(pin=8):
    GPIO.setup(pin ,GPIO.in)
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.out)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def pump_on(pump_pin=7):
    init_output(pump_pin)
    GPIO.output(pump_pin, GPIO.HIGH)
    f=open('last_watered.txt',"w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()

def auto_water():
    while True:
        status=get_status()
        if status==1:
            init_output(pump_pin)
            GPIO.output(pump_pin, GPIO.HIGH)           
        else:
            GPIO.output(pump_pin, GPIO.LOW)
            break





