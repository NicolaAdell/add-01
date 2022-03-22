from machine import Pin
from time import sleep
l1= Pin(1, Pin.OUT)
p1= Pin(28, Pin.IN)
p2= Pin(27, Pin.IN)
l2= Pin(2, Pin.OUT)


while True: 
  if p1.value() == 1:
    l1.on()
  else:
    l1.off()
  while p2.value() == 1:
    l2.on()
    sleep(.5)
    if p2.value() == 1:
      l2.off()
      sleep(.5)
  else:
    pass