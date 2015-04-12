import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)


x=0;
while x!=318:
	GPIO.output(11,1)
	GPIO.output(12,1)
	GPIO.output(13,1)
	GPIO.output(15,1)
	time.sleep(0.00115)
	GPIO.output(11,0)
	GPIO.output(12,0)
	GPIO.output(13,0)
	GPIO.output(15,0)
	time.sleep(0.002)
	x=x+1

"""
lasts 1 second
sets arm to vertical state
does not change claw
does not slow as approaches destination
"""


x=0;
while x!=345:
	GPIO.output(11,1)
	GPIO.output(12,1)
	time.sleep(0.0009)
	GPIO.output(11,0)
	GPIO.output(12,0)
	time.sleep(.002)
"""
lasts 1 second
sets servo 1 to approximately 75 degrees
sets servo 2 to approximately 75 degrees
does not slow as approaches destination
"""

x=0;
while x!=345:
	GPIO.output(11,1)
	GPIO.output(12,1)
	time.sleep(0.0005)
	GPIO.output(16,1)
	times.sleep(0.0004)
	GPIO.output(11,0)
	GPIO.output(12,0)
	GPIO.output(16,0)
	time.sleep(.002)
"""
lasts 1 second
holds servo 1 at approximately 75 degrees
holds servo 2 at approximately 75 degrees
closes claw
does not slow as approaches destination
"""

x=0;
while x!=294:
	GPIO.output(11,1)
	time.sleep(0.00065)
	GPIO.output(12,1)
	time.sleep(0.00035)
	GPIO.output(16,1)
	times.sleep(0.0004)
	GPIO.output(11,0)
	GPIO.output(12,0)
	GPIO.output(16,0)
	time.sleep(.002)
"""
lasts 1 second
pulls servo 1(base servo) back to approximately 110 degrees while moving servo 2 forward so a to lessen stress on servo 1
claw remains closed
does not slow as approaches destination
"""

x=0;
while x!=318:
	GPIO.output(11,1)
	GPIO.output(12,1)
	GPIO.output(13,1)
	GPIO.output(15,1)
	time.sleep(0.00075)
	GPIO.output(16,1)
	time.sleep(0.0004)
	GPIO.output(11,0)
	GPIO.output(12,0)
	GPIO.output(13,0)
	GPIO.output(15,0)
	GPIO.output(16,0)
	time.sleep(0.002)
	x=x+1

"""
lasts 1 second
sets arm to vertical state
claw remains closed
does not slow as approaches destination
"""


