import threading
import time


def ping():
	while True:
		time.sleep(0.2)
		with lock:
			print("ping =====================")


def pong():
	while True:
		time.sleep(0.2)
		with lock:
			print("pong =============================================")


# не работает должным образом при помощи блокировок

lock = threading.RLock()
# lock = threading.Lock()

task1 = threading.Thread(target=ping)
task2 = threading.Thread(target=pong)

task1.start()
time.sleep(0.1)
task2.start()

task1.join()
task2.join()