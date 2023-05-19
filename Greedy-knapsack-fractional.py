class item():
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.c = v/w
    
    def __lt__(self, other):
        return self.cost < other.cost

if __name__ == "__main__":
    w = [15, 10, 2, 4]
    v = [30, 25, 2, 6]
    m = 10
    n = 4
    
def knapsack(w, v, m, n):
    packs = []
    