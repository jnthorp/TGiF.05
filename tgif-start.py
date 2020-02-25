import os
import argparse
from os.path import join
import sys
import datetime
import re
import subprocess

if __name__ == "__main__":
	expDir = os.getcwd()
	scriptsDir = os.path.join(expDir,'Scripts')

	# parse input args
	parser = argparse.ArgumentParser(description='run this script to initiate any part of the TGIF task')
	parser.add_argument('section', nargs='*', help='items = pre-conditioning; scenes = conditioning; demo = test-demo; test = test')
	args = parser.parse_args()
	if args.section[1].endswith('items'):
		script = os.path.join(scriptsDir, 'pre-conditioning.py')
		python_call = ['python', script]
		subprocess.call(python_call)

	if args.section[1].endswith('scenes'):
		script = os.path.join(scriptsDir, 'conditioning.py')
		python_call = ['python', script]
		subprocess.call(python_call)

	if args.section[1].endswith('demo'):
		script = os.path.join(scriptsDir, 'test-demo.py')
		python_call = ['python', script]
		subprocess.call(python_call)

	if args.section[1].endswith('test'):
		script = os.path.join(scriptsDir, 'test.py')
		python_call = ['python', script]
		subprocess.call(python_call)

