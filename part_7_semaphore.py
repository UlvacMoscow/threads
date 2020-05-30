import threading
import time


def producer():
	current_thread = threading.current_thread()
	with lock:
		print("Get locking", lock._value)
		print(current_thread.getName())
		time.sleep(3)
		print("I'm free")


max_workers = 3
lock = threading.BoundedSemaphore(value=max_workers)

task1 = threading.Thread(target=producer, name="task1")
task2 = threading.Thread(target=producer, name="task2")
task3 = threading.Thread(target=producer, name="task3")
task4 = threading.Thread(target=producer, name="task4")

task1.start()
task2.start()
task3.start()
task4.start()

task1.join()
task2.join()
task3.join()
task4.join()
