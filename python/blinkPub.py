#!/usr/bin/env python
import zmq
from msgpack import unpackb, packb, loads
import numpy as np
import cv2
import pyttsx3

from pymouse import PyMouse

currentId = -1

if __name__ == "__main__":

	m = PyMouse()

	context = zmq.Context()
	# open a req port to talk to pupil
	addr = '127.0.0.1'  # remote ip or localhost
	req_port = "50020"  # same as in the pupil remote gui
	req = context.socket(zmq.REQ)
	req.setsockopt(zmq.LINGER, 0)
	req.connect("tcp://{}:{}".format(addr, req_port))

	# ask for the sub port
	req.send_string('SUB_PORT')
	sub_port = req.recv_string()

	# open a sub port to listen to pupil
	sub = context.socket(zmq.SUB)
	sub.connect("tcp://{}:{}".format(addr, sub_port))

	# set subscriptions to topics
	# recv just pupil/gaze/notifications
	sub.setsockopt_string(zmq.SUBSCRIBE, "blinks")

	recent_world = None

	FRAME_FORMAT = 'bgr' #Image format, same as the one in Pupil Capture
	eyeCloseFlag = False
	startTime = 0
	endTime = 0	
	
	while True:
		#ret, frame = cap.read()
		try:
			print("loop")
			topic = sub.recv_string()
			msg = sub.recv()
			msg = loads(msg, raw=False)
			print("\n{}: {}".format(topic,msg))
			if msg['type'] == 'onset' and not eyeCloseFlag:
				eyeCloseFlag = True
				startTime = msg['timestamp']
			if msg['type'] == 'offset' and eyeCloseFlag:
				eyeCloseFlag = False
				endTime = msg['timestamp']
				duration = endTime - startTime
				if duration > 2.0 and duration < 3.0:
					m.click(m.position()[0], m.position()[1])
				else:
					endTime = 0
					startTime = 0
					duration = 0
				
		except KeyboardInterrupt:
			break
		
	print("Terminated")
	req.close()
	sub.close()
	context.term()


	
	

