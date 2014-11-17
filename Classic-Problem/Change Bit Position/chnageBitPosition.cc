#include<iostream>


using namespace std;

void printBinary(int number){

	int cmp=1<<31;
	int x;
	int cnt=32;
	while(cnt>0){
		x=(number & cmp)?1:0;
		cout<<x;
		number=number<<1;
		cnt--;
	}
}


int getChnagedN(int N,int M,int i,int j){

	int bitPatternI=1<<i;
	int bitPatternJ=1<<j;

	int MI=M | ~bitPatternI;	//Bits at position i is that of M, all others are 1.
	int MJ=M | ~bitPatternJ;

	int MIJ=MI & MJ;	//Bits at position i and j are that of M, all others are 1.

	int ans=N & MIJ;

	return ans;
}


int main(){

	int N=48;
	int M=8;

	cout<<endl;
	cout<<"N :"<<N<<" M :"<<M<<endl<<endl;
	cout<<"N :";
	printBinary(N);
	cout<<endl;
	cout<<"M :";
	printBinary(M);

	cout<<endl;
	cout<<endl;

	int i=4, j=6;
	cout<<"i :"<<i<<" j :"<<j;

	int ans=getChnagedN(N,M,i,j);

	cout<<endl;
	cout<<endl;

	printBinary(ans);

	cout<<endl;
	cout<<endl;

	return 0;
}
