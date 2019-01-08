# This Script Uses adb commands to poll the status of the phone battery.
# It then uses matplotlib to plot the voltage and current over time.

import subprocess
from datetime import datetime
import time

# Holds plot data
timestamps = []
voltages = []
currents = []

while (true):
	# Get battery info by using a system call
	battery_stat = subprocess.check_output(['adb', '-d', 'shell', 'dumpsys', 'battery']).decode('utf-8')
	battery_stat = list(map(lambda el: el.strip(), battery_stat.split('\n')))

	# Find voltage and current & push to array
	time = datetime.now().time()
	for element in battery_stat:
		if 'voltage' in element
			print(element)
		elif 'current' in element
			print(current)

	time.sleep(30)
