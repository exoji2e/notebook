#include <vector>
#include <iostream>
using namespace std;
class ST;

class ST {
	public:
		int li,ri,sum; //sum can be changed for max,min etc
		ST *lN, *rN;
};
ST* makeSgmTree(vector<int> *A1, int l, int r) {
	vector<int> A = *A1;
	if (l==r) {
		static ST node;
		node.li=l;
		node.ri=r;
		node.sum=A[l];
		return &node;
	}
	int mid = (l+r)/2;
	ST *lN1 = makeSgmTree(&A,l,mid);
	ST *rN1 = makeSgmTree(&A,mid+1,r);
	ST lN=*lN1;
	ST rN=*rN1;
	static ST root;
	root.li=lN.li;
	root.ri=rN.ri;
	root.sum=lN.sum+rN.sum; //or respective operator
	root.lN=&lN;
	root.rN=&rN;
	return &root;
}
int getSum(ST *root1, int l, int r) {
	ST root = *root1;
	if (root.li>=l && root.ri<=r) return root.sum;
	if (root.ri<l || root.li>r) return 0; //or respective neutral element
	return getSum(root.lN,l,r) + getSum(root.rN,l,r); //or respective operator
}
int update(ST *root1, int i, int val) {
	ST root = *root1;
	int diff = 0;
	if (root.li==root.ri && i==root.li) {
		diff=val-root.sum;//max/min
		root.sum=val;//max/min
		return diff; //root.max
	}
	int mid=(root.ri+root.li)/2;
	if (i<=mid) diff = update(root.lN,i,val);
	else diff = update(root.rN,i,val);
	root.sum+= diff; //max/min
	return diff; //max/min
}

int main(){
	int temp[] = {0,50,25,80,32};
	vector<int> A;
	A.insert(A.begin(),temp,temp+5);
	ST *root = makeSgmTree(&A,0,4);
	
	cout << getSum(root,0,4) << endl; //should print 187
	cout << getSum((*root).lN,0,4) << endl;
	cout << getSum(root,1,4) << endl; //also 187
	cout << getSum(root, 4,4) << endl; //32
	update(root,2,30);
	cout << getSum(root, 2,4) << endl; //should print 142
	return 0;
}

