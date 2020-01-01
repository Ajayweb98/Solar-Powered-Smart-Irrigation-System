import RPi.GPIO as GPIO
import water
import datetime

GPIO.setmode(GPIO.BOARD)

if __name__ == "__main__":
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    status=water.get_status()
    while True:
        while status==1:
            status=water.get_status()
            GPIO.output(7, GPIO.LOW)
            f = open("last_watered.txt", "w")
            f.write("Last watered {}".format(datetime.datetime.now()))
            f.close()
        while status==0:
            status=water.get_status()
            GPIO.output(7, GPIO.HIGH)
