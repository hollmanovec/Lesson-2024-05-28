import threading
import time

# THREADS AND SOCKETS

#Task 1

# The user types in values in a list, After that, two threads start. The first thread finds the largest value in the list
# the second thread finds the smallest value. The results are displayed on the screen.

user_list = []

while True:
    number = input("Zadejte číslo do seznamu. Pro konec zadejte [OK]")
    if number == "OK":
        break
    number = int(number)
    user_list.append(number)


def find_max():
    print(f"Největší hodnota: {max(user_list)}")


def find_min():
    print(f"Nejmenší hodnota {min(user_list)}")


thread1 = threading.Thread(target=find_max, name="Vlákno1")
thread2 = threading.Thread(target=find_min, name="Vlákno2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()