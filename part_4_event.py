import threading
import time


def producer():
	while True:
		time.sleep(0.2)
		product.set()
		product.clear()
		print("Ping ------------------------")


def consumer():
	while True:
		product.wait()
		print("Pong +++++++++++++++++++++++++++++")


product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task2.start()
task1.start()

task2.join()
task1.join()