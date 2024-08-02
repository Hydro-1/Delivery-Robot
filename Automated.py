# External module imports
import RPi.GPIO as GPIO
from time import time, sleep

# Define the GPIO pins for motor control
IN1 = 21
IN2 = 20
IN3 = 16
IN4 = 13
ENA = 12

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

pwm = GPIO.PWM(ENA, 100)
pwm.start(0)

# Define GPIO pins for ultrasonic central
GPIO_ECHO = 2
GPIO_TRIGGER = 3
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO, GPIO.IN)      # Echo < In

# Drive control functions
def goForward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(75)

def turnLeft():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(75)

def turnRight():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(75)

def goBackward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm.ChangeDutyCycle(75)

def stop_motors():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

# Detect obstacles
def frontobstacle():
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)
    
    # Allow module to settle
    sleep(0.2)
    
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_CENTRAL, True)
    sleep(0.00001)
    
    GPIO.output(GPIO_TRIGGER_CENTRAL, False)
    
    start = time()
    
    while GPIO.input(GPIO_ECHO_CENTRAL) == 0:
        start = time()
    
    while GPIO.input(GPIO_ECHO_CENTRAL) == 1:
        stop = time()
    
    # Calculate pulse length
    elapsed = stop - start
    
    # Distance pulse travelled in that time is time, multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000 / 2  # distance of both directions so divide by 2
    print("Front Distance : %.1f" % distance)

    return distance

# Check front obstacle and turn right if there is an obstacle
def checkanddrivefront():
    while frontobstacle() < 30:
        global prev_turn
        stop_motors()
        
        if prev_turn == 'left':
            prev_turn = 'right'
            turnright()
            
        elif prev_turn == 'right':
            prev_turn == 'left'
            turnleft()

    goForward()

# Avoid obstacles and drive forward
def obstacle_avoidance_drive()():
    goforward()

    start = time.time()

    # Hard limit drive time of 5 minutes
    while start > time.time() - 300:  # 300 = 60 seconds * 5
        if frontobstacle() < 30:
            stop_motors()
            # Check front side - turn right or left if obstructed 
            checkanddrivefront()

    # Clear GPIOs, it will stop motors       
    cleargpios()


def cleargpios():
    GPIO.output(2, False)
    GPIO.output(3, False)
    GPIO.output(23, False)
    GPIO.output(24, False)
    GPIO.output(27, False)
    GPIO.output(22, False)
    GPIO.output(25, False)    

def main():
    cleargpios()
    print("Driving...")
    
    # Start obstacle avoidance driving
    obstacle_avoidance_drive()

if __name__ == "__main__":
    global prev_turn = 'left'
    main()