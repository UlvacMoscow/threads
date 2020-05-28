import threading
import time


def hander(started=0, finished=0):
	result = 0
	for el in range(started, finished):
		result += 1
	print("Values ", result)


params = {'finished': 2 ** 26}

task = threading.Thread(target=hander, kwargs=params)
start_time = time.time()
print('Reslut 1')
task.start()
task.join()
print('Time: {}'.format(time.time() - start_time)) 

start_time = time.time()
print('Result 2')
hander(**params)
print('Time: {}'.format(time.time() - start_time)) 

