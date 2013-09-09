
import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)


class ledpixels():
	def __init__():

		self.ledpixels = [0] * 25
		
		colorwipe(self.ledpixels, Color(255, 0, 0), 0.02)
		colorwipe(self.ledpixels, Color(0, 255, 0), 0.02)
		colorwipe(self.ledpixels, Color(0, 0, 255), 0.02)
		colorwipe(self.ledpixels, Color(0, 0, 0), 0.02)

	def writestrip(pixels):
		spidev = file("/dev/spidev0.0", "w")
		for i in range(len(pixels)):
			spidev.write(chr((pixels[i]>>16) & 0xFF))
			spidev.write(chr((pixels[i]>>8) & 0xFF))
			spidev.write(chr(pixels[i] & 0xFF))
		spidev.close()
		time.sleep(0.002)

	def Color(r, g, b):
		return ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)

	def setpixelcolor(pixels, n, r, g, b):
		if (n >= len(pixels)):
			return
		pixels[n] = Color(r,g,b)

	def setpixelcolor(pixels, n, c):
		if (n >= len(pixels)):
			return
		pixels[n] = c

	def colorwipe(pixels, c, delay):
		for i in range(len(pixels)):
			setpixelcolor(pixels, i, c)
			writestrip(pixels)
			time.sleep(delay)		

	def Wheel(WheelPos):
		if (WheelPos < 85):
	   		return Color(WheelPos * 3, 255 - WheelPos * 3, 0)
		elif (WheelPos < 170):
	   		WheelPos -= 85;
	   		return Color(255 - WheelPos * 3, 0, WheelPos * 3)
		else:
			WheelPos -= 170;
			return Color(0, WheelPos * 3, 255 - WheelPos * 3)

	def rainbowCycle(pixels, wait):
		for j in range(256): # one cycle of all 256 colors in the wheel
	    	   for i in range(len(pixels)):
	# tricky math! we use each pixel as a fraction of the full 96-color wheel
	# (thats the i / strip.numPixels() part)
	# Then add in j which makes the colors go around per pixel
	# the % 96 is to make the wheel cycle around
	      		setpixelcolor(pixels, i, Wheel( ((i * 256 / len(pixels)) + j) % 256) )
		   writestrip(pixels)
		   time.sleep(wait)

