import random

class QuickUnion:

    def __init__(self, N):
        self.ids = [i for i in range(N)]

    def find_root(self, x):
        root = x
        while self.ids[root]!=root:
            root = self.ids[root]
        return root

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def union(self, p, q):
        self.ids[self.find_root(p)]=self.find_root(q)

    def print_status(self):
        print(self.ids)


qf = QuickUnion(10)
random.randint(0,10)
for i in range(10):
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
    
