import threading
import time 



receptionest = threading.Semaphore(5)

def enter_examRoom(n):
    print(f"patiant {n} is waiting for his turn")
    receptionest.acquire()
    print(f"patiant {n} is in the examiniation room")
    time.sleep(2)
    print(f"patiant {n} is out of the examiniation room")
    receptionest.release()


patiants=[]

for i in range(10):
    patiant=threading.Thread(target=enter_examRoom,args=(i,))
    patiants.append(patiant)
    patiant.start()
