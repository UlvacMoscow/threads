import threading


print(threading.active_count())
current_thread = threading.current_thread()
print(current_thread.getName())
print(current_thread.is_alive())

try:
	current_thread.start()
except RuntimeError as e:
	print(e)

current_thread.setName('NewName')
print(current_thread.getName())

current_thread.name = "NewName2"
print(current_thread.getName())
print(current_thread.name)

#выводит все живые и запущенные треды
print(threading.enumerate())
