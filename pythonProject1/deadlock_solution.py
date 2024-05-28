import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()
all_lock = threading.Lock()
# Funkcia, ktorá spôsobí deadlock
def deadlock_function1():
    # v pripade vice zamku udelat managera
    # ktery ma ako kriticku sekci i prave
    # pozamykani prislusnych zamecku
    with all_lock:
        lock1.acquire()
        print("Thread 1 získalo lock1")
        lock2.acquire()
        print("Thread 1 získalo lock2")
    # pozor na poradi uzamykani zdroju
    # taky resi problem

    time.sleep(1)

    lock1.release()
    lock2.release()
    print("release f2")

# Funkcia, ktorá spôsobí deadlock
def deadlock_function2():
    with all_lock:
        lock1.acquire()
        print("Thread 2 získalo lock1")
        lock2.acquire()
        print("Thread 2 získalo lock2")

    time.sleep(1)

    lock2.release()
    lock1.release()
    print("release f2")

thread1 = threading.Thread(target=deadlock_function1)
thread2 = threading.Thread(target=deadlock_function2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()