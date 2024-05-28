import threading
import time
# Globální proměnná sdílená mezi vlákny
balance = 1000
lock = threading.Lock()

# Funkce reprezentující transakci
def make_transaction(amount):
    global balance
    lock.acquire()
    current_balance = balance


    # Simulace nějakého výpočtu nebo operace
    # Mezitím může jiné vlákno změnit hodnotu balance
    # a tím způsobit race condition
    time.sleep(0.1)
    try:
        balance = current_balance - amount
    finally:
        lock.release()


# Vytvoření dvou vláken pro provedení transakcí
thread1 = threading.Thread(target=make_transaction, args=(200,))
thread2 = threading.Thread(target=make_transaction, args=(300,))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

# Očekávaný výsledek je 500, ale může být odlišný kvůli race condition
print("Zůstatek na účtu po transakcích:", balance)