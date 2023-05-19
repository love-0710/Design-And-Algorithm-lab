#include <stdlib.h>
#include <stdio.h>
#include<iostream>

using namespace std;

int lcs(string X, string Y, int m, int n)
{
        int L[m + 1][n + 1];
        int P[m+1][n+1];
        for (int i = 0; i <= m; i++) {
                for (int j = 0; j <= n; j++) {
                        if (i == 0 || j == 0)
                                L[i][j] = 0;
                        else if (X[i - 1] == Y[j - 1])
                                {L[i][j] = L[i - 1][j - 1] + 1;
                                P[i][j]=1;
                        }
                        else
                                if(L[i-1][j]>=L[i][j-1])
                                {
                                        L[i][j]=L[i-1][j];
                                        P[i][j]=0;
                                }
                                else
                                {
                                        L[i][j]=L[i][j-1];
                                        P[i][j]=2;
                                }
                }
        }
        string k="";
        int i=m,j=n;
        while(i!=0 && j!=0){
                if(P[i][j]==1){
                        k=X[i-1]+k;
                        i-=1;
                        j-=1;
                }
                else if(P[i][j]==0)
                        i-=1;
                else
                        j-=1;
        }
        cout<<k<<endl;
        return L[m][n];
}

int main()
{
        string S1 = "TEACHERS";
        string S2 = "TEARS";
        int m = S1.size();
        int n = S2.size();
        int t=lcs(S1, S2, m, n);
        cout << "Length of LCS is " << t;
        return 0;
}

