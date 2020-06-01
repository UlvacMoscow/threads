from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time


def handler(started=0, finished=0):
	result = 0
	for i in range(started, finished):
		result += 1
	return result


def run_by_exexutor(executor_class, max_workers=4):
	executor = executor_class(max_workers=max_workers)
	started = time.time()
	future1 = executor.submit(handler, started=0, finished=2 ** 26)
	future2 = executor.submit(handler, started=2 ** 26, finished=2 ** 28)

	result = future2.result() + future1.result()
	print("Result {result}, Time for {executor}: {spent_time}".format(
			result=result,
			executor=executor_class.__name__,
			spent_time=time.time() - started
		)
	)

