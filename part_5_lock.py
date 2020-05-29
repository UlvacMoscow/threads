import threading


def producer():
	print("Get locking")
	with lock:
		print("done lock")
		with lock:
			print("unknown lock")
	print("locking release")




lock = threading.Lock()

task1 = threading.Thread(target=producer)

task1.start()

task1.join()