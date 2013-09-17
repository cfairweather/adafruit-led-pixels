
import RPi.GPIO as GPIO, time, os
import datetime
import time



ledpixels_T_COLOR = 0;
ledpixels_T_GRADI = 1;
ledpixels_T_FLASH = 2;

ledpixels_example = [
		[{"type":ledpixels_T_COLOR,"time":0,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_COLOR,"time":1,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_GRADI,"time":0,"color":{"r":0,"g":0,"b":0},"time_end":1,"color_end":{"r":255,"g":0,"b":0}}, {"type":ledpixels_T_COLOR,"time":1,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_GRADI,"time":1,"color":{"r":0,"g":0,"b":0},"time_end":2,"color_end":{"r":0,"g":255,"b":20}}, {"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_GRADI,"time":2,"color":{"r":0,"g":0,"b":0},"time_end":3,"color_end":{"r":0,"g":28,"b":255}}, {"type":ledpixels_T_COLOR,"time":3,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_FLASH,"time":0,"time_end":1,"color":{"r":255,"g":0,"b":0}, "period":0.2}, {"type":ledpixels_T_COLOR,"time":1,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_FLASH,"time":1,"time_end":2,"color":{"r":0,"g":255,"b":20}, "period":0.2}, {"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_FLASH,"time":2,"time_end":3,"color":{"r":0,"g":28,"b":255}, "period":0.2}, {"type":ledpixels_T_COLOR,"time":3,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_COLOR,"time":0,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_COLOR,"time":1,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_GRADI,"time":0,"color":{"r":0,"g":0,"b":0},"time_end":1,"color_end":{"r":255,"g":0,"b":0}}, {"type":ledpixels_T_COLOR,"time":1,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_GRADI,"time":1,"color":{"r":0,"g":0,"b":0},"time_end":2,"color_end":{"r":0,"g":255,"b":20}}, {"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_GRADI,"time":2,"color":{"r":0,"g":0,"b":0},"time_end":3,"color_end":{"r":0,"g":28,"b":255}}, {"type":ledpixels_T_COLOR,"time":3,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_FLASH,"time":0,"time_end":1,"color":{"r":255,"g":0,"b":0}, "period":0.2}, {"type":ledpixels_T_COLOR,"time":1,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_FLASH,"time":1,"time_end":2,"color":{"r":0,"g":255,"b":20}, "period":0.2}, {"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_FLASH,"time":2,"time_end":3,"color":{"r":0,"g":28,"b":255}, "period":0.2}, {"type":ledpixels_T_COLOR,"time":3,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_COLOR,"time":0,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_COLOR,"time":1,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_GRADI,"time":0,"color":{"r":0,"g":0,"b":0},"time_end":1,"color_end":{"r":255,"g":0,"b":0}}, {"type":ledpixels_T_COLOR,"time":1,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_GRADI,"time":1,"color":{"r":0,"g":0,"b":0},"time_end":2,"color_end":{"r":0,"g":255,"b":20}}, {"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_GRADI,"time":2,"color":{"r":0,"g":0,"b":0},"time_end":3,"color_end":{"r":0,"g":28,"b":255}}, {"type":ledpixels_T_COLOR,"time":3,"color":{"r":0,"g":28,"b":255},"time_end":5}]
		]


class Pixels():
	def __init__(self):
		DEBUG = 1
		GPIO.setmode(GPIO.BCM)

		self.pixels = [0] * 25

		# self.colorwipe(Color(255, 0, 0), 0.001)
		# self.colorwipe(Color(0, 255, 0), 0.001)
		# self.colorwipe(Color(0, 0, 255), 0.001)
		self.colorwipe(Color(0, 0, 0), 0.001)

	def writestrip(self):
		# print "Writing pixels: "+str(self.pixels)
		spidev = file("/dev/spidev0.0", "w")
		for i in range(len(self.pixels)):
			spidev.write(chr((self.pixels[i]>>16) & 0xFF))
			spidev.write(chr((self.pixels[i]>>8) & 0xFF))
			spidev.write(chr(self.pixels[i] & 0xFF))
		spidev.close()
		time.sleep(0.001)


	def setpixelcolor(self, n, r, g, b):
		if (n >= len(self.pixels)):
			return
		self.pixels[n] = Color(r,g,b)

	def setpixelcolor(self, n, c):
		if (n >= len(self.pixels)):
			return
		self.pixels[n] = c

	def colorwipe(self, c, delay):
		for i in range(len(self.pixels)):
			self.setpixelcolor(i, c)
			self.writestrip()
			time.sleep(delay)		


	def rainbowCycle(self, wait):
		for j in range(256): # one cycle of all 256 colors in the wheel
	    	   for i in range(len(self.pixels)):
				# tricky math! we use each pixel as a fraction of the full 96-color wheel
				# (thats the i / strip.numself.Pixels() part)
				# Then add in j which makes the colors go around per pixel
				# the % 96 is to make the wheel cycle around
	      		self.setpixelcolor(i, Wheel( ((i * 256 / len(self.pixels)) + j) % 256) )
		   self.writestrip()
		   time.sleep(wait)

# const int T_COLOR = 0;
# const int T_GRADI = 1;
# const int T_FLASH = 2;
	
	def example(self):
		self.run(ledpixels_example, 8)

	def run(self, tracks, duration):
		index_marker = []
		for t in range(len(tracks)):
			index_marker.append(0)

		time_start = time.time()
		time_curr  = time.time()

		time_elapsed = time_curr - time_start

		while time_elapsed < duration+1:

			time_curr  = time.time()
			time_elapsed = time_curr - time_start
			# print "\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\nTime elapsed: "+str(time_elapsed)

			self.writestrip()

			for t in range(len(tracks)):
				# print "Track "+str(t)
				seg_wasSet = False

				track = tracks[t]
				for d in range(index_marker[t], len(track)):
					# print "Checking segment "+str(d)
					segment = track[d]
					seg_time = segment['time']
					seg_time_end = segment['time_end']


					if seg_time <= time_elapsed and seg_time_end >= time_elapsed:

						seg_wasSet = True

						seg_color = Color(max(segment['color']['r'],0),max(segment['color']['g'],0), max(segment['color']['b'],0))
						seg_type = segment['type']

						if seg_type==ledpixels_T_COLOR:
							# print "Setting Color self.setpixelcolor("+str(t)+", "+str(seg_color)+")"
							self.setpixelcolor(t, seg_color)

						elif seg_type==ledpixels_T_GRADI:
							seg_duration = seg_time_end - seg_time
							seg_progress_perc = (time_elapsed - seg_time )*1.0/(seg_duration*1.0)
							seg_progress_iprc = 1.0-seg_progress_perc

							seg_color_compd = Color(segment['color']['r']*(seg_progress_iprc)+max(segment['color_end']['r'],0)*(seg_progress_perc),
													segment['color']['g']*(seg_progress_iprc)+max(segment['color_end']['g'],0)*(seg_progress_perc), 
													segment['color']['b']*(seg_progress_iprc)+max(segment['color_end']['b'],0)*(seg_progress_perc))

							self.setpixelcolor(t, seg_color_compd)

						elif seg_type==ledpixels_T_FLASH:
							seg_period = segment['period'] 
							seg_progress = time_elapsed - seg_time 
							seg_period_fit = ((seg_progress * 10.0) % (seg_period * 10.0)) / 10.0

							if seg_period_fit < seg_period / 2.0:
								self.setpixelcolor(t, seg_color)
							else:
								self.setpixelcolor(t,Color_black)

						break #go to next track


					elif seg_time_end <= time_elapsed:
						index_marker[t] = d 

				#We need to hit at least one segment and break, if not, set to black 
				if not seg_wasSet:
					self.setpixelcolor(t, Color_black) 
						
			


def Wheel(WheelPos):
	if (WheelPos < 85):
   		return Color(WheelPos * 3, 255 - WheelPos * 3, 0)
	elif (WheelPos < 170):
   		WheelPos -= 85;
   		return Color(255 - WheelPos * 3, 0, WheelPos * 3)
	else:
		WheelPos -= 170;
		return Color(0, WheelPos * 3, 255 - WheelPos * 3)

def Color(r, g, b):
	return ((int(r) & 0xFF) << 16) | ((int(g) & 0xFF) << 8) | (int(b) & 0xFF)

Color_black = Color(0,0,0)
