import threading


def exec_ping_pong():
	png = threading.Timer(0.1, ping) #отложенный старт	
	png.start()

def ping():
	print("ping =======================================")
	png = threading.Timer(0.1, pong)
	png.start()

def pong():
	print("pong ==================")
	exec_ping_pong()

exec_ping_pong()
