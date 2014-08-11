#include<iostream>

using namespace std;

int main(){
	int ary[5]={3,8,5,4,7};

	int lowerIndex=0;
	int upperIndex=4;
	int equilibriumIndex=0;
	int lowerSum=ary[lowerIndex++];
	int upperSum=ary[upperIndex--];

	while(lowerIndex<upperIndex){
		if(lowerSum<upperSum){
			lowerSum+=ary[lowerIndex++];
			equilibriumIndex=lowerIndex;
		}
		else if (lowerSum>upperSum){
			upperSum+=ary[upperIndex--];
			equilibriumIndex=upperIndex;
		}

	}

	if(lowerSum==upperSum){
		cout<<"Equilibrium Index is "<<equilibriumIndex<<endl;
	}
	else{
		cout<<"No Equilibrium Point Found"<<endl;
	}

}
