#include<iostream>

using namespace std;

int value[]={60,100,120};
int weight[]={10,20,30};

int KnapSack(int itemIndex, int capacity);


int main(){

	int capacity=50;

	for(int i=0;i<3;i++){
		cout<<weight[i]<<" ";

	}

	int maximumValue=KnapSack(0, capacity);
	cout<<endl<<"Value gathered is :"<<maximumValue<<endl;

	return 0;
}


int KnapSack(int itemIndex, int capacity){

	if(itemIndex==3)
		return 0;

	int itemWeight=weight[itemIndex];
	int itemValue=value[itemIndex];


	int itemExcluded=KnapSack(itemIndex+1, capacity);


	if(capacity<itemWeight){	//If weight of item is more than remaining capacity, it should be excluded.
		return itemExcluded;
	}

	int itemIncluded=itemValue+KnapSack(itemIndex+1, capacity-itemWeight);

	if(itemIncluded>itemExcluded){	//If includeing item generates more value than excluding it, lets include that.
		return itemIncluded;
	}
	else{
		return itemExcluded;
	}

}
