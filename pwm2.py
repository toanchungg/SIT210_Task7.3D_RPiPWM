import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 18
GPIO_ECHO = 24
ledpin = 12

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)
pi_pwm.start(0)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if(dist<15):
                pi_pwm.ChangeDutyCycle(1)
            elif(14<dist<25):
                pi_pwm.ChangeDutyCycle(15)
            elif(24<dist<35):
                pi_pwm.ChangeDutyCycle(35)
            elif(34<dist<60):
                pi_pwm.ChangeDutyCycle(65))
            else:
                pi_pwm.ChangeDutyCycle(100)
            time.sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()
