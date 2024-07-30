### Motor Control ###

import RPi.GPIO as GPIO
from time import sleep

# Define the GPIO pins for motor control
IN1 = 21
IN2 = 20
IN3 = 16
IN4 = 13
ENA = 12

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

pwm = GPIO.PWM(ENA, 100)
pwm.start(0)

# Define the motor control functions
def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(75)

def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm.ChangeDutyCycle(75)
    
def right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(75)
    
def left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(75)
    
def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

# Begin execution
try:
    while True:
        forward()
        sleep(2)
        stop()
        sleep(1)
        backward()
        sleep(2)
        stop()
        sleep(1)
        left()
        sleep(2)
        right()
        sleep(2)

# Press 'CTRL + C' to stop execution
except KeyboardInterrupt:
    GPIO.cleanup()
    stop()
