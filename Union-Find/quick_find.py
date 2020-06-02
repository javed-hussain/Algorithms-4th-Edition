import random

class QuickFind:
    
    def __init__(self, N):
        self.ids = [i for i in range(N)]

    def connected(self,p,q):
        return self.ids[p]==self.ids[q]

    def union(self, p, q):
        pid = self.ids[p]
        qid = self.ids[q]

        for i in range(len(self.ids)):
            if self.ids[i]==pid:
                self.ids[i]=qid

    def print_status(self):
        print(self.ids)

qf = QuickFind(10)
random.randint(0,10)
for i in range(5):
    p = random.randint(0,9)
    q = random.randint(0,9)
    # print(f'\np = {p:<10}q = {q}')
    qf.union(p,q)
    # qf.print_status()

qf.print_status()
for i in range(5):
    p = random.randint(0,9)
    q = random.randint(0,9)
    print(f'\np = {p:<10}q = {q}')
    print(qf.connected(p,q))
    
