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
	cout<<endl;
}


int printChnagedN(int N,int M,int i,int j){

	int bitPatternI=1<<i;
	int bitPatternJ=1<<j;

	int MI=M & bitPatternI;
	int MJ=M & bitPatternJ;

	int MIJ;
	if(i==j)
		MIJ=MI;
	else
		MIJ=MI | MJ;

	int negatedMIJ=!MIJ;

	int tempAns=N & negatedMIJ;

	tempAns=tempAns | MIJ;

	return tempAns;
}


int main(){

	int N=48;
	int M=8;

	printBinary(N);
	cout<<endl;
	printBinary(M);

	cout<<endl;
	cout<<endl;

	int i=4, j=6;

	int ans=printChnagedN(N,M,i,j);

	printBinary(ans);

	return 0;
}
