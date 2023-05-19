def towerofhanoi(n, s, d, a):
        if n==0:
                return
        towerofhanoi(n-1, s, a, d)
        print("move disk",n, "from ", s, "to", d)
        towerofhanoi(n-1, a, d, s)
n=3
towerofhanoi(n , 's', 'd', 'a' )
