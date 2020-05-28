import threading
import time


def hander(started=0, finished=0):
	result = 0
	for el in range(started, finished):
		result += 1
	results.append(result)


results = []

task1 = threading.Thread(target=hander, kwargs={"finished": 2 ** 13})
task2 = threading.Thread(target=hander, kwargs={"started": 2 ** 13, "finished": 2 ** 26})

start_time = time.time()

task1.start()
task2.start()

task1.join()
task2.join()


print("results 1")
print('Time: {}'.format(time.time() - start_time)) 
print("Values ", sum(results))

results = []

start_time = time.time()
hander(finished=2 ** 26)

print('Result 2')
print('Time: {}'.format(time.time() - start_time)) 
print("Values ", sum(results))

