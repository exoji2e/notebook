#include <iostream>
#include <vector>
using namespace std;
//assumes s.size()>=w.size()
bool kmp(vector<int> *w1, vector<int> *s1) {
	vector<int> w = *w1;
	vector<int> s = *s1;
	vector<int> T;
	T.assign(w.size(),0);
	T[0]=-1;
	int m=0; int i=2;
	while (i<w.size()) {
		if (w[i-1]==w[m]) {
			T[i]=++m;
			i++;
		} else if (m>0) {
			m=T[m];
		} else {
			T[i]=0;
			i++;
		}
	}
	m=0; i=0;
	while (m+i<s.size()){
		if (w[i]==s[m+i]) {
			if(i==w.size()-1) return true;
			i++;
		} else if (T[i] > -1) {
			m=m+i-T[i];
			i=T[i];
		} else {
			i=0;
			m=m+1;
		}
	}
	return false;
}
int main(){
	vector<int> w,s;
	s.assign(5, 2);
	s.push_back(8);
	w.push_back(2);
	w.push_back(8);
	cout << kmp(&w,&s) << endl; //prints "1"
	return 0;
}	
