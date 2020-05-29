import threading


# пример работы потокобезопасного хранилища данных
current_thread = threading.current_thread()
data = threading.local()
data.value = 10

def print_result():
	print(threading.current_thread())
	print("Local value of thread {}".format(data.value))


def counter(started, value):
	print(hasattr(data, "value"))
	data.value = started
	for i in range(value):
		data.value += 1
	print_result()

task1 = threading.Thread(target=counter, args=(0, 20), name="Task1")
task2 = threading.Thread(target=counter, args=(50, 5), name="Task2")

task1.start()
task2.start()

print_result()
print("Threads alivies {}, and count thread = {}".format(threading.enumerate(), threading.active_count()))


task1.join()
task2.join()

print_result()
print("Threads alivies {}, and count thread = {}".format(threading.enumerate(), threading.active_count()))
