
import RPi.GPIO as GPIO, time, os
import datetime
import time



ledpixels_T_COLOR = 0;
ledpixels_T_GRADI = 1; #color_end
ledpixels_T_FLASH = 2; #period
ledpixels_T_CHASE = 3; #period, #pixel_from, #pixel_to
ledpixels_T_CHASE_GRAD = 4; #period, #pixel_from, #pixel_to, #color_end

ledpixels_demo_basic = [
		[{"type":ledpixels_T_COLOR,"time":0,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_COLOR,"time":1,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_GRADI,"time":0,"color":{"r":0,"g":0,"b":0},"time_end":1,"color_end":{"r":255,"g":0,"b":0}}, {"type":ledpixels_T_COLOR,"time":1,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_GRADI,"time":1,"color":{"r":0,"g":0,"b":0},"time_end":2,"color_end":{"r":0,"g":255,"b":20}}, {"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_GRADI,"time":2,"color":{"r":0,"g":0,"b":0},"time_end":3,"color_end":{"r":0,"g":28,"b":255}}, {"type":ledpixels_T_COLOR,"time":3,"color":{"r":0,"g":28,"b":255},"time_end":5}],
		[{"type":ledpixels_T_FLASH,"time":0,"time_end":1,"color":{"r":255,"g":0,"b":0}, "period":0.05}, {"type":ledpixels_T_COLOR,"time":1,"color":{"r":255,"g":0,"b":0},"time_end":3}],
		[{"type":ledpixels_T_FLASH,"time":1,"time_end":2,"color":{"r":0,"g":255,"b":20}, "period":0.05}, {"type":ledpixels_T_COLOR,"time":2,"color":{"r":0,"g":255,"b":20},"time_end":4}],
		[{"type":ledpixels_T_FLASH,"time":2,"time_end":3,"color":{"r":0,"g":28,"b":255}, "period":0.05}, {"type":ledpixels_T_COLOR,"time":3,"color":{"r":0,"g":28,"b":255},"time_end":5}],
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

ledpixels_demo_chasing_lights = [
		[{"type":ledpixels_T_COLOR,"time":0.0,"color":{"r":255,"g":0,"b":0},"time_end":0.1}, {"type":ledpixels_T_COLOR,"time":1.0,"color":{"r":0,"g":255,"b":0},"time_end":1.1}, {"type":ledpixels_T_COLOR,"time":2.0,"color":{"r":0,"g":0,"b":255},"time_end":2.1}],
		[{"type":ledpixels_T_COLOR,"time":0.1,"color":{"r":255,"g":0,"b":0},"time_end":0.2}, {"type":ledpixels_T_COLOR,"time":1.1,"color":{"r":0,"g":255,"b":0},"time_end":1.2}, {"type":ledpixels_T_COLOR,"time":2.1,"color":{"r":0,"g":0,"b":255},"time_end":2.2}],
		[{"type":ledpixels_T_COLOR,"time":0.2,"color":{"r":255,"g":0,"b":0},"time_end":0.3}, {"type":ledpixels_T_COLOR,"time":1.2,"color":{"r":0,"g":255,"b":0},"time_end":1.3}, {"type":ledpixels_T_COLOR,"time":2.2,"color":{"r":0,"g":0,"b":255},"time_end":2.3}],
		[{"type":ledpixels_T_COLOR,"time":0.3,"color":{"r":255,"g":0,"b":0},"time_end":0.4}, {"type":ledpixels_T_COLOR,"time":1.3,"color":{"r":0,"g":255,"b":0},"time_end":1.4}, {"type":ledpixels_T_COLOR,"time":2.3,"color":{"r":0,"g":0,"b":255},"time_end":2.4}],
		[{"type":ledpixels_T_COLOR,"time":0.4,"color":{"r":255,"g":0,"b":0},"time_end":0.5}, {"type":ledpixels_T_COLOR,"time":1.4,"color":{"r":0,"g":255,"b":0},"time_end":1.5}, {"type":ledpixels_T_COLOR,"time":2.4,"color":{"r":0,"g":0,"b":255},"time_end":2.5}],
		[{"type":ledpixels_T_COLOR,"time":0.5,"color":{"r":255,"g":0,"b":0},"time_end":0.6}, {"type":ledpixels_T_COLOR,"time":1.5,"color":{"r":0,"g":255,"b":0},"time_end":1.6}, {"type":ledpixels_T_COLOR,"time":2.5,"color":{"r":0,"g":0,"b":255},"time_end":2.6}],
		[{"type":ledpixels_T_COLOR,"time":0.6,"color":{"r":255,"g":0,"b":0},"time_end":0.7}, {"type":ledpixels_T_COLOR,"time":1.6,"color":{"r":0,"g":255,"b":0},"time_end":1.7}, {"type":ledpixels_T_COLOR,"time":2.6,"color":{"r":0,"g":0,"b":255},"time_end":2.7}],
		[{"type":ledpixels_T_COLOR,"time":0.7,"color":{"r":255,"g":0,"b":0},"time_end":0.8}, {"type":ledpixels_T_COLOR,"time":1.7,"color":{"r":0,"g":255,"b":0},"time_end":1.8}, {"type":ledpixels_T_COLOR,"time":2.7,"color":{"r":0,"g":0,"b":255},"time_end":2.8}],
		[{"type":ledpixels_T_COLOR,"time":0.8,"color":{"r":255,"g":0,"b":0},"time_end":0.9}, {"type":ledpixels_T_COLOR,"time":1.8,"color":{"r":0,"g":255,"b":0},"time_end":1.9}, {"type":ledpixels_T_COLOR,"time":2.8,"color":{"r":0,"g":0,"b":255},"time_end":2.9}],
		[{"type":ledpixels_T_COLOR,"time":0.9,"color":{"r":255,"g":0,"b":0},"time_end":1.1}, {"type":ledpixels_T_COLOR,"time":1.9,"color":{"r":0,"g":255,"b":0},"time_end":2.0}, {"type":ledpixels_T_COLOR,"time":2.9,"color":{"r":0,"g":0,"b":255},"time_end":3.0}],
		[{"type":ledpixels_T_COLOR,"time":1.0,"color":{"r":255,"g":0,"b":0},"time_end":1.1}, {"type":ledpixels_T_COLOR,"time":2.0,"color":{"r":0,"g":255,"b":0},"time_end":2.1}, {"type":ledpixels_T_COLOR,"time":3.0,"color":{"r":0,"g":0,"b":255},"time_end":3.1}],
		[{"type":ledpixels_T_COLOR,"time":1.1,"color":{"r":255,"g":0,"b":0},"time_end":1.2}, {"type":ledpixels_T_COLOR,"time":2.1,"color":{"r":0,"g":255,"b":0},"time_end":2.2}, {"type":ledpixels_T_COLOR,"time":3.1,"color":{"r":0,"g":0,"b":255},"time_end":3.2}],
		[{"type":ledpixels_T_COLOR,"time":1.2,"color":{"r":255,"g":0,"b":0},"time_end":1.3}, {"type":ledpixels_T_COLOR,"time":2.2,"color":{"r":0,"g":255,"b":0},"time_end":2.3}, {"type":ledpixels_T_COLOR,"time":3.2,"color":{"r":0,"g":0,"b":255},"time_end":3.3}],
		[{"type":ledpixels_T_COLOR,"time":1.3,"color":{"r":255,"g":0,"b":0},"time_end":1.4}, {"type":ledpixels_T_COLOR,"time":2.3,"color":{"r":0,"g":255,"b":0},"time_end":2.4}, {"type":ledpixels_T_COLOR,"time":3.3,"color":{"r":0,"g":0,"b":255},"time_end":3.4}],
		[{"type":ledpixels_T_COLOR,"time":1.4,"color":{"r":255,"g":0,"b":0},"time_end":1.5}, {"type":ledpixels_T_COLOR,"time":2.4,"color":{"r":0,"g":255,"b":0},"time_end":2.5}, {"type":ledpixels_T_COLOR,"time":3.4,"color":{"r":0,"g":0,"b":255},"time_end":3.5}],
		[{"type":ledpixels_T_COLOR,"time":1.5,"color":{"r":255,"g":0,"b":0},"time_end":1.6}, {"type":ledpixels_T_COLOR,"time":2.5,"color":{"r":0,"g":255,"b":0},"time_end":2.6}, {"type":ledpixels_T_COLOR,"time":3.5,"color":{"r":0,"g":0,"b":255},"time_end":3.6}],
		[{"type":ledpixels_T_COLOR,"time":1.6,"color":{"r":255,"g":0,"b":0},"time_end":1.7}, {"type":ledpixels_T_COLOR,"time":2.6,"color":{"r":0,"g":255,"b":0},"time_end":2.7}, {"type":ledpixels_T_COLOR,"time":3.6,"color":{"r":0,"g":0,"b":255},"time_end":3.7}],
		[{"type":ledpixels_T_COLOR,"time":1.7,"color":{"r":255,"g":0,"b":0},"time_end":1.8}, {"type":ledpixels_T_COLOR,"time":2.7,"color":{"r":0,"g":255,"b":0},"time_end":2.8}, {"type":ledpixels_T_COLOR,"time":3.7,"color":{"r":0,"g":0,"b":255},"time_end":3.8}],
		[{"type":ledpixels_T_COLOR,"time":1.8,"color":{"r":255,"g":0,"b":0},"time_end":1.9}, {"type":ledpixels_T_COLOR,"time":2.8,"color":{"r":0,"g":255,"b":0},"time_end":2.9}, {"type":ledpixels_T_COLOR,"time":3.8,"color":{"r":0,"g":0,"b":255},"time_end":3.9}],
		[{"type":ledpixels_T_COLOR,"time":1.9,"color":{"r":255,"g":0,"b":0},"time_end":2.0}, {"type":ledpixels_T_COLOR,"time":2.9,"color":{"r":0,"g":255,"b":0},"time_end":3.0}, {"type":ledpixels_T_COLOR,"time":3.9,"color":{"r":0,"g":0,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_COLOR,"time":2.0,"color":{"r":255,"g":0,"b":0},"time_end":2.1}, {"type":ledpixels_T_COLOR,"time":3.0,"color":{"r":0,"g":255,"b":0},"time_end":3.1}, {"type":ledpixels_T_COLOR,"time":4.0,"color":{"r":0,"g":0,"b":255},"time_end":4.1}],
		[{"type":ledpixels_T_COLOR,"time":2.1,"color":{"r":255,"g":0,"b":0},"time_end":2.2}, {"type":ledpixels_T_COLOR,"time":3.1,"color":{"r":0,"g":255,"b":0},"time_end":3.2}, {"type":ledpixels_T_COLOR,"time":4.1,"color":{"r":0,"g":0,"b":255},"time_end":4.2}],
		[{"type":ledpixels_T_COLOR,"time":2.2,"color":{"r":255,"g":0,"b":0},"time_end":2.3}, {"type":ledpixels_T_COLOR,"time":3.2,"color":{"r":0,"g":255,"b":0},"time_end":3.3}, {"type":ledpixels_T_COLOR,"time":4.2,"color":{"r":0,"g":0,"b":255},"time_end":4.3}],
		[{"type":ledpixels_T_COLOR,"time":2.3,"color":{"r":255,"g":0,"b":0},"time_end":2.4}, {"type":ledpixels_T_COLOR,"time":3.3,"color":{"r":0,"g":255,"b":0},"time_end":3.4}, {"type":ledpixels_T_COLOR,"time":4.3,"color":{"r":0,"g":0,"b":255},"time_end":4.4}],
		[{"type":ledpixels_T_COLOR,"time":2.4,"color":{"r":255,"g":0,"b":0},"time_end":2.5}, {"type":ledpixels_T_COLOR,"time":3.4,"color":{"r":0,"g":255,"b":0},"time_end":3.5}, {"type":ledpixels_T_COLOR,"time":4.4,"color":{"r":0,"g":0,"b":255},"time_end":4.5}],
		]

ledpixels_demo_chasing_flashing = [
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.0,"color":{"r":255,"g":0,"b":0},"time_end":0.1}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.0,"color":{"r":0,"g":255,"b":0},"time_end":1.1}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":0,"g":0,"b":255},"time_end":2.1}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.1,"color":{"r":255,"g":0,"b":0},"time_end":0.2}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.1,"color":{"r":0,"g":255,"b":0},"time_end":1.2}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.1,"color":{"r":0,"g":0,"b":255},"time_end":2.2}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.2,"color":{"r":255,"g":0,"b":0},"time_end":0.3}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.2,"color":{"r":0,"g":255,"b":0},"time_end":1.3}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.2,"color":{"r":0,"g":0,"b":255},"time_end":2.3}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.3,"color":{"r":255,"g":0,"b":0},"time_end":0.4}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.3,"color":{"r":0,"g":255,"b":0},"time_end":1.4}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.3,"color":{"r":0,"g":0,"b":255},"time_end":2.4}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.4,"color":{"r":255,"g":0,"b":0},"time_end":0.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.4,"color":{"r":0,"g":255,"b":0},"time_end":1.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.4,"color":{"r":0,"g":0,"b":255},"time_end":2.5}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.5,"color":{"r":255,"g":0,"b":0},"time_end":0.6}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.5,"color":{"r":0,"g":255,"b":0},"time_end":1.6}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.5,"color":{"r":0,"g":0,"b":255},"time_end":2.6}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.6,"color":{"r":255,"g":0,"b":0},"time_end":0.7}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.6,"color":{"r":0,"g":255,"b":0},"time_end":1.7}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.6,"color":{"r":0,"g":0,"b":255},"time_end":2.7}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.7,"color":{"r":255,"g":0,"b":0},"time_end":0.8}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.7,"color":{"r":0,"g":255,"b":0},"time_end":1.8}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.7,"color":{"r":0,"g":0,"b":255},"time_end":2.8}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.8,"color":{"r":255,"g":0,"b":0},"time_end":0.9}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.8,"color":{"r":0,"g":255,"b":0},"time_end":1.9}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.8,"color":{"r":0,"g":0,"b":255},"time_end":2.9}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.9,"color":{"r":255,"g":0,"b":0},"time_end":1.1}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.9,"color":{"r":0,"g":255,"b":0},"time_end":2.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.9,"color":{"r":0,"g":0,"b":255},"time_end":3.0}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.0,"color":{"r":255,"g":0,"b":0},"time_end":1.1}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":0,"g":255,"b":0},"time_end":2.1}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.0,"color":{"r":0,"g":0,"b":255},"time_end":3.1}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.1,"color":{"r":255,"g":0,"b":0},"time_end":1.2}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.1,"color":{"r":0,"g":255,"b":0},"time_end":2.2}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.1,"color":{"r":0,"g":0,"b":255},"time_end":3.2}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.2,"color":{"r":255,"g":0,"b":0},"time_end":1.3}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.2,"color":{"r":0,"g":255,"b":0},"time_end":2.3}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.2,"color":{"r":0,"g":0,"b":255},"time_end":3.3}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.3,"color":{"r":255,"g":0,"b":0},"time_end":1.4}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.3,"color":{"r":0,"g":255,"b":0},"time_end":2.4}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.3,"color":{"r":0,"g":0,"b":255},"time_end":3.4}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.4,"color":{"r":255,"g":0,"b":0},"time_end":1.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.4,"color":{"r":0,"g":255,"b":0},"time_end":2.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.4,"color":{"r":0,"g":0,"b":255},"time_end":3.5}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.5,"color":{"r":255,"g":0,"b":0},"time_end":1.6}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.5,"color":{"r":0,"g":255,"b":0},"time_end":2.6}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.5,"color":{"r":0,"g":0,"b":255},"time_end":3.6}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.6,"color":{"r":255,"g":0,"b":0},"time_end":1.7}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.6,"color":{"r":0,"g":255,"b":0},"time_end":2.7}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.6,"color":{"r":0,"g":0,"b":255},"time_end":3.7}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.7,"color":{"r":255,"g":0,"b":0},"time_end":1.8}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.7,"color":{"r":0,"g":255,"b":0},"time_end":2.8}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.7,"color":{"r":0,"g":0,"b":255},"time_end":3.8}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.8,"color":{"r":255,"g":0,"b":0},"time_end":1.9}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.8,"color":{"r":0,"g":255,"b":0},"time_end":2.9}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.8,"color":{"r":0,"g":0,"b":255},"time_end":3.9}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":1.9,"color":{"r":255,"g":0,"b":0},"time_end":2.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.9,"color":{"r":0,"g":255,"b":0},"time_end":3.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.9,"color":{"r":0,"g":0,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":255,"g":0,"b":0},"time_end":2.1}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.0,"color":{"r":0,"g":255,"b":0},"time_end":3.1}, {"type":ledpixels_T_FLASH, "period":0.05,"time":4.0,"color":{"r":0,"g":0,"b":255},"time_end":4.1}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":2.1,"color":{"r":255,"g":0,"b":0},"time_end":2.2}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.1,"color":{"r":0,"g":255,"b":0},"time_end":3.2}, {"type":ledpixels_T_FLASH, "period":0.05,"time":4.1,"color":{"r":0,"g":0,"b":255},"time_end":4.2}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":2.2,"color":{"r":255,"g":0,"b":0},"time_end":2.3}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.2,"color":{"r":0,"g":255,"b":0},"time_end":3.3}, {"type":ledpixels_T_FLASH, "period":0.05,"time":4.2,"color":{"r":0,"g":0,"b":255},"time_end":4.3}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":2.3,"color":{"r":255,"g":0,"b":0},"time_end":2.4}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.3,"color":{"r":0,"g":255,"b":0},"time_end":3.4}, {"type":ledpixels_T_FLASH, "period":0.05,"time":4.3,"color":{"r":0,"g":0,"b":255},"time_end":4.4}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":2.4,"color":{"r":255,"g":0,"b":0},"time_end":2.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.4,"color":{"r":0,"g":255,"b":0},"time_end":3.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":4.4,"color":{"r":0,"g":0,"b":255},"time_end":4.5}],
		]


ledpixels_demo_police = [
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.0,"color":{"r":255,"g":0,"b":0},"time_end":0.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.0,"color":{"r":255,"g":0,"b":0},"time_end":1.5},{"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":255,"g":0,"b":0},"time_end":2.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.0,"color":{"r":255,"g":0,"b":0},"time_end":3.5}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.0,"color":{"r":255,"g":0,"b":0},"time_end":0.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.0,"color":{"r":255,"g":0,"b":0},"time_end":1.5},{"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":255,"g":0,"b":0},"time_end":2.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.0,"color":{"r":255,"g":0,"b":0},"time_end":3.5}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.0,"color":{"r":255,"g":0,"b":0},"time_end":0.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.0,"color":{"r":255,"g":0,"b":0},"time_end":1.5},{"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":255,"g":0,"b":0},"time_end":2.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.0,"color":{"r":255,"g":0,"b":0},"time_end":3.5}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.0,"color":{"r":255,"g":0,"b":0},"time_end":0.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.0,"color":{"r":255,"g":0,"b":0},"time_end":1.5},{"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":255,"g":0,"b":0},"time_end":2.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.0,"color":{"r":255,"g":0,"b":0},"time_end":3.5}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.0,"color":{"r":255,"g":0,"b":0},"time_end":0.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.0,"color":{"r":255,"g":0,"b":0},"time_end":1.5},{"type":ledpixels_T_FLASH, "period":0.05,"time":2.0,"color":{"r":255,"g":0,"b":0},"time_end":2.5}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.0,"color":{"r":255,"g":0,"b":0},"time_end":3.5}],
		
		
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_CHASE,"period":0.033333333333333,"pixel_from":5, "pixel_to":19,  "time":0.0,"color":{"r":255,"g":255,"b":255},"time_end":4.0}],

		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.5,"color":{"r":0,"g":0,"b":255},"time_end":1.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.5,"color":{"r":0,"g":0,"b":255},"time_end":2.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.5,"color":{"r":0,"g":0,"b":255},"time_end":3.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.5,"color":{"r":0,"g":0,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.5,"color":{"r":0,"g":0,"b":255},"time_end":1.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.5,"color":{"r":0,"g":0,"b":255},"time_end":2.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.5,"color":{"r":0,"g":0,"b":255},"time_end":3.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.5,"color":{"r":0,"g":0,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.5,"color":{"r":0,"g":0,"b":255},"time_end":1.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.5,"color":{"r":0,"g":0,"b":255},"time_end":2.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.5,"color":{"r":0,"g":0,"b":255},"time_end":3.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.5,"color":{"r":0,"g":0,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.5,"color":{"r":0,"g":0,"b":255},"time_end":1.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.5,"color":{"r":0,"g":0,"b":255},"time_end":2.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.5,"color":{"r":0,"g":0,"b":255},"time_end":3.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.5,"color":{"r":0,"g":0,"b":255},"time_end":4.0}],
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.5,"color":{"r":0,"g":0,"b":255},"time_end":1.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":1.5,"color":{"r":0,"g":0,"b":255},"time_end":2.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":2.5,"color":{"r":0,"g":0,"b":255},"time_end":3.0}, {"type":ledpixels_T_FLASH, "period":0.05,"time":3.5,"color":{"r":0,"g":0,"b":255},"time_end":4.0}],
		]

ledpixels_demo_mindfuck = [
		[{"type":ledpixels_T_FLASH, "period":0.05,"time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.06,"time":0.0,"color":{"r":100,"g":100,"b":110},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.07,"time":0.0,"color":{"r":100,"g":100,"b":120},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.08,"time":0.0,"color":{"r":100,"g":100,"b":130},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.09,"time":0.0,"color":{"r":100,"g":100,"b":140},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.10,"time":0.0,"color":{"r":100,"g":100,"b":150},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.11,"time":0.0,"color":{"r":100,"g":100,"b":160},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.12,"time":0.0,"color":{"r":100,"g":100,"b":170},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.13,"time":0.0,"color":{"r":100,"g":100,"b":180},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.14,"time":0.0,"color":{"r":100,"g":100,"b":190},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.15,"time":0.0,"color":{"r":100,"g":110,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.16,"time":0.0,"color":{"r":100,"g":120,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.17,"time":0.0,"color":{"r":100,"g":130,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.18,"time":0.0,"color":{"r":100,"g":140,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.19,"time":0.0,"color":{"r":100,"g":150,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.20,"time":0.0,"color":{"r":100,"g":160,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.21,"time":0.0,"color":{"r":100,"g":170,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.22,"time":0.0,"color":{"r":100,"g":180,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.23,"time":0.0,"color":{"r":100,"g":190,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.24,"time":0.0,"color":{"r":110,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.25,"time":0.0,"color":{"r":120,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.26,"time":0.0,"color":{"r":130,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.27,"time":0.0,"color":{"r":140,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.28,"time":0.0,"color":{"r":150,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_FLASH, "period":0.29,"time":0.0,"color":{"r":160,"g":100,"b":100},"time_end":5.0}],
		]

ledpixels_demo_chasing_feature = [
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE, "period":0.02,"pixel_from":0, "pixel_to":24, "time":0.0,"color":{"r":100,"g":100,"b":100},"time_end":5.0}],
		]

ledpixels_demo_chasing_gradient = [
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		[{"type":ledpixels_T_CHASE_GRAD, "period":0.05,"pixel_from":1, "pixel_to":20, "time":0.0,"color":{"r":255,"g":0,"b":0},"color_end":{"r":0,"g":0,"b":255},"time_end":5.0}],
		]


class Pixels():
	def __init__(self):
		DEBUG = 1
		GPIO.setmode(GPIO.BCM)

		self.pixels = [0] * 25
		self.demos = [
			{"name":"Basic", "data":ledpixels_demo_basic, "duration":9},
			{"name":"Chasing Lights", "data":ledpixels_demo_chasing_lights, "duration":6},
			{"name":"Flashing Chasing Lights", "data":ledpixels_demo_chasing_flashing, "duration":6},
			{"name":"Flashing Police", "data":ledpixels_demo_police, "duration":4.0},
			{"name":"Flashing Mindfuck", "data":ledpixels_demo_mindfuck, "duration":5.0},
			{"name":"Chasing Simple", "data":ledpixels_demo_chasing_feature, "duration":5.1},
			{"name":"Chasing Gradient", "data":ledpixels_demo_chasing_gradient, "duration":5.1},
		]

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
		self.run(ledpixels_demo_basic, 8)

	def demo(self, index):
		print "Playing demo: "+self.demos[index]['name']
		self.run(self.demos[index]['data'], self.demos[index]['duration'])

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
					segment 	= track[d]
					seg_time 	= segment['time']
					seg_time_end= segment['time_end']


					if seg_time <= time_elapsed and seg_time_end >= time_elapsed:

						seg_wasSet = True

						seg_color = Color(max(segment['color']['r'],0),max(segment['color']['g'],0), max(segment['color']['b'],0))
						seg_type = segment['type']

						if seg_type==ledpixels_T_COLOR:
							# print "Setting Color self.setpixelcolor("+str(t)+", "+str(seg_color)+")"
							self.setpixelcolor(t, seg_color)

						elif seg_type==ledpixels_T_GRADI:
							seg_duration 		= seg_time_end - seg_time
							seg_progress_perc 	= (time_elapsed - seg_time )*1.0/(seg_duration*1.0)
							seg_progress_iprc 	= 1.0-seg_progress_perc

							seg_color_compd = Color(segment['color']['r']*(seg_progress_iprc)+max(segment['color_end']['r'],0)*(seg_progress_perc),
													segment['color']['g']*(seg_progress_iprc)+max(segment['color_end']['g'],0)*(seg_progress_perc), 
													segment['color']['b']*(seg_progress_iprc)+max(segment['color_end']['b'],0)*(seg_progress_perc))

							self.setpixelcolor(t, seg_color_compd)

						elif seg_type==ledpixels_T_FLASH:
							seg_period 		= segment['period'] 
							seg_progress 	= time_elapsed - seg_time 
							seg_period_fit 	= ((seg_progress * 10.0) % (seg_period * 10.0)) / 10.0

							if seg_period_fit < seg_period / 2.0:
								self.setpixelcolor(t, seg_color)
							else:
								self.setpixelcolor(t,Color_black)

						elif seg_type==ledpixels_T_CHASE:
							seg_progress= time_elapsed - seg_time 
							seg_period 	= segment['period'] 
							p_from 		= segment['pixel_from']
							p_to 		= segment['pixel_to']
							p_range 	= abs(p_from-p_to)+1

							seg_progress_mod = seg_progress % (seg_period*p_range)

							# period = 0.1, from=0, to=9, time_end=2, progress= 0.6
							if seg_progress_mod>=((t-p_from)*seg_period) and seg_progress_mod<((t-p_from+1)*seg_period) and t >=p_from and t<=p_to:
								# print str(seg_progress_mod)+">="+str((t*seg_period)) + " and < "+str(((t+1)*seg_period))
								self.setpixelcolor(t, seg_color)
							else:
								seg_wasSet = False

						elif seg_type==ledpixels_T_CHASE_GRAD:
							seg_duration 		= seg_time_end - seg_time
							seg_progress_perc 	= (time_elapsed - seg_time )*1.0/(seg_duration*1.0)
							seg_progress_iprc 	= 1.0-seg_progress_perc

							seg_color_compd = Color(segment['color']['r']*(seg_progress_iprc)+max(segment['color_end']['r'],0)*(seg_progress_perc),
													segment['color']['g']*(seg_progress_iprc)+max(segment['color_end']['g'],0)*(seg_progress_perc), 
													segment['color']['b']*(seg_progress_iprc)+max(segment['color_end']['b'],0)*(seg_progress_perc))

							seg_progress= time_elapsed - seg_time 
							seg_period 	= segment['period'] 
							p_from 		= segment['pixel_from']
							p_to 		= segment['pixel_to']
							p_range 	= abs(p_from-p_to)+1

							seg_progress_mod = seg_progress % (seg_period*p_range)

							# period = 0.1, from=0, to=9, time_end=2, progress= 0.6
							if seg_progress_mod>=((t-p_from)*seg_period) and seg_progress_mod<((t-p_from+1)*seg_period) and t >=p_from and t<=p_to:
								# print str(seg_progress_mod)+">="+str((t*seg_period)) + " and < "+str(((t+1)*seg_period))
								self.setpixelcolor(t, seg_color_compd)
							else:
								seg_wasSet = False




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

p = Pixels()
