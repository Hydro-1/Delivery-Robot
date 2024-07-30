### Ultrasonic Sensor Integration ###

from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo=17, trigger=27)

# Begin execution
try:
    while True:
      print(ultrasonic.distance)
      sleep(0.1)
      
# Press 'CTRL + C' to stop execution
except KeyboardInterrupt:
    print("Distance reading stopped!)
    break

