from gpiozero import LED
from time import sleep



led01 = LED(17)
led02 = LED(27)
led03 = LED(22)


while True:
	led01.on()
	sleep(1)
	led01.off()
	led02.on()
	sleep(1)
	led02.off()
	led03.on()
	sleep(1)
