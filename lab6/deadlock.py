import threading
def worker1(lock1, lock2): 
    with lock1:
        print("DEBUG: lock1 acquired, waiting for lock2")
        while not lock2.locked(): 
            print('tes1') #ensuring deadlock for demo with lock2:
        print("In critical section")
def worker2(lock1, lock2): 
    with lock2:
        print("DEBUG: lock2 acquired, waiting for lock1")
        while not lock1.locked(): 
            print('test2') #ensuring deadlock for demo with lock1:
            pass
        print("In critical section")
if __name__ == "__main__": 
    mutex1 = threading.Lock() 
    mutex2 = threading.Lock()
    threading.Thread(target=worker1, args=(mutex1, mutex2)).start() 
    threading.Thread(target=worker2, args=(mutex1, mutex2)).start() #join omitted to be concise