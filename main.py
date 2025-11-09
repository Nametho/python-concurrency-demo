import threading

cond = threading.Condition()
liste = []

def waiter(cond, liste):
    cond.acquire()
    while len(liste) == 0:
        cond.wait()
    print("le mot de passe est:", liste.pop())
    cond.release()

t1 = threading.Thread(target=waiter, args=(cond, liste))
t2 = threading.Thread(target=waiter, args=(cond, liste))
t3 = threading.Thread(target=waiter, args=(cond, liste))
t4 = threading.Thread(target=waiter, args=(cond, liste))
t5 = threading.Thread(target=waiter, args=(cond, liste))

threads = [t1, t2, t3, t4, t5]

for t in threads:
    t.start()

for i in range(0, 5):
    cond.acquire()
    mdp = input("Entrez un mot de passe:")
    liste.append(mdp)
    cond.notify()
    cond.release()