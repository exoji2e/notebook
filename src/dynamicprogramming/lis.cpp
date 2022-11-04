#include <iostream>
#include <vector>
using namespace std;
int lis(vector<int> *X1) {
	vector<int> X = *X1;
	int n = X.size();
	vector<int> P, M;
	P.assign(n,0);
	M.assign(n+1,0);
	int L=0;
	for (int i = 0; i<n; i++) {
		int lo =1;
		int hi = L;
		while (lo<=hi) {
			int mid = lo+(hi-lo+1)/2;
			if (X[M[mid]]<X[i]) lo=mid+1;
			else hi=mid-1;
		}
		int newL=lo;
		P[i]=M[newL-1];
		M[newL]=i;
		if (newL>L) L=newL;
	}
	vector<int> S;
	S.assign(L,0);
	int k = M[L];
	for (int i = L-1; i>=0; i--) {
		S[i]=k; //or X[k]
		k=P[k];
	}
	return L; //or S
}
int main() {
	vector<int> X;
	for (int i = 0; i<10; i++)  X.push_back(i);
	cout << lis(&X) << endl; //prints "10"	

	return 0;
}
