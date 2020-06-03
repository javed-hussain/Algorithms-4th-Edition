import random

class WeightedQuickUnion:
    
    def __init__(self, N):
        self.ids = [i for i in range(N)]
        self.tree_sizes = [1]*N

    def find_root(self, x):
        root = x
        while self.ids[root]!=root:
            self.ids[root] = self.ids[self.ids[root]]
            root = self.ids[root]
        return root

    def union(self, p, q):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if p_root==q_root:
            return
        if self.tree_sizes[p_root] >= self.tree_sizes[q_root]:
            self.ids[q_root]=p_root
            self.tree_sizes[q_root]+=self.tree_sizes[p_root]
        else:
            self.ids[p_root]=self.find_root(q_root)
            self.tree_sizes[p_root]+=self.tree_sizes[q_root]

    def eavluate_sizes(self):
        for i in range(len(self.ids)):
            root = i
            s = 1
            while self.ids[root]!=root:
                root = self.ids[root]
                s+=1
            self.tree_sizes[i]=s

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)
    
    def print_status(self):
        print(self.ids)

N=100
wqu = WeightedQuickUnion(N)
for i in range(N*(N//2)):
    p = random.randint(0,N-1)
    q = random.randint(0,N-1)
    # print(f'\np = {p:<10}q = {q}')
    wqu.union(p,q)
    # wqu.print_status()
    # print(wqu.tree_sizes)

# wqu.print_status()
# for i in range(N/2):
#     p = random.randint(0,N=1)
#     q = random.randint(0,N-1)
#     print(f'\np = {p:<10}q = {q}')
#     print(wqu.connected(p,q))
wqu.eavluate_sizes()
print(max(wqu.tree_sizes))
print(wqu.tree_sizes)