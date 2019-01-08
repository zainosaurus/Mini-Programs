# This Script Uses adb commands to poll the status of the phone battery.
# It then uses matplotlib to plot the voltage and current over time.

import subprocess
from datetime import datetime
import time
import re

# Holds plot data
timestamps = []
voltages = []
currents = []

while (True):
	# Get battery info by using a system call
	battery_stat = subprocess.check_output(['adb', '-d', 'shell', 'dumpsys', 'battery']).decode('utf-8')
	battery_stat = list(map(lambda el: el.strip(), battery_stat.split('\n')))

	# Find voltage and current & push to array
	cur_time = datetime.now().time()
	for element in battery_stat:
		v = re.match(r'voltage: *(\d+)', element)
		c = re.match(r'current now: *(-?\d+)', element)
		if v != None:
			voltage = v.group(1)
		elif c != None:
			current = c.group(1)

	print(cur_time, voltage, current)
	time.sleep(5)

