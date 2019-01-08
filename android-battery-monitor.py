# This Script Uses adb commands to poll the status of the phone battery.
# It then uses matplotlib to plot the voltage and current over time.

import subprocess
import time
import re
import matplotlib.pyplot as plt
import signal

DELAY = 2

def exit_sequence(sig, frame):
	print('Program Killed by SIGINT')
	plt.close()
	plt.show(block=True)

signal.signal(signal.SIGINT, exit_sequence)

def replot(x_data, c_data, v_data):
	plt.gcf().clear()
	plt.plot(x_data, c_data, 'g')
	plt.xlabel('Time Elapsed (s)')
	plt.ylabel('Current (mA)')
	plt.pause(0.0001)
	plt.show(block=False)

# Holds plot data
timestamps = []
voltages = []
currents = []

cur_time = 0
while (True):
	# Get battery info by using a system call
	battery_stat = subprocess.check_output(['adb', '-s', '192.168.10.16:5555', 'shell', 'dumpsys', 'battery']).decode('utf-8')
	battery_stat = list(map(lambda el: el.strip(), battery_stat.split('\n')))

	timestamps.append(cur_time)
	# Find voltage and current & push to array
	for element in battery_stat:
		v = re.match(r'voltage: *(\d+)', element)
		c = re.match(r'current now: *(-?\d+)', element)

		if v != None:
			voltage = v.group(1)
			voltages.append(float(voltage))
		elif c != None:
			current = c.group(1)
			currents.append(float(current))
	# print(timestamps, currents, voltages)
	# print(str(cur_time) + '\t\t' + str(voltage) + '\t\t' + str(current))
	replot(timestamps, currents, voltages)
	cur_time += DELAY
	time.sleep(DELAY)


