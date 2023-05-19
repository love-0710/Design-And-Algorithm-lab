def lcs(X , Y, m, n):
        L = [[None]*(n+1) for i in range(m+1)]
        P= [[None]*(n+1) for i in range(m+1)]
        k=""
        for i in range(m+1):
                for j in range(n+1):
                        if i == 0 or j == 0 :
                                L[i][j] = 0
                        elif X[i-1] == Y[j-1]:
                                P[i][j]="D"
                                L[i][j] = L[i-1][j-1]+1
                        else:
                                if(L[i-1][j]>=L[i][j-1]):
                                        L[i][j]=L[i-1][j]
                                        P[i][j]="T"
                                elif(L[i][j-1]>=L[i-1][j]):
                                        L[i][j]=L[i-1][j]
                                        P[i][j]="L"
        i=m
        j=n
        while i!=0 and j!=0:
                if P[i][j]=="D":
                        k=X[i-1]+k
                        i=i-1
                        j=j-1
                elif P[i][j]=="T":
                        i=i-1
                else:
                        j=j-1
        print(k)
        return L[m][n]



if __name__ == '__main__':
        S1 = "TEACHERS"
        S2 = "TEARS"
        m = len(S1)
        n = len(S2)
        print ("Length of LCS is", lcs(S1, S2, m, n) )
