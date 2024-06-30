import threading
import time

def print_status(thread_number, stop_event):
    start_time = time.time()
    while not stop_event.is_set():
        elapsed_time = int(time.time() - start_time)
        print(f"Thread {thread_number} is running at {elapsed_time} seconds")
        time.sleep(5)


stop_event1 = threading.Event()
stop_event2 = threading.Event()
stop_event3 = threading.Event()


thread1 = threading.Thread(target=print_status, args=(1, stop_event1))
thread2 = threading.Thread(target=print_status, args=(2, stop_event2))
thread3 = threading.Thread(target=print_status, args=(3, stop_event3))


thread1.start()
thread3.start()


time.sleep(20)
stop_event1.set()
thread2.start()

time.sleep(18)
stop_event3.set()
stop_event1.clear()
thread1 = threading.Thread(target=print_status, args=(1, stop_event1))
thread1.start()


time.sleep(60)
