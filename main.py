from machine import Pin
from time import sleep
l1= Pin(1, Pin.OUT)
s1= Pin(28, Pin.IN)
s2= Pin(27, Pin.IN)
l2= Pin(2, Pin.OUT)


while True: 
  if s1.value() == 1:
    l1.on()
  else:
    l1.off()
  while s2.value() == 1:
    l2.on()
    sleep(.5)
    if s2.value() == 1:
      l2.off()
      sleep(.5)
  else:
    pass
