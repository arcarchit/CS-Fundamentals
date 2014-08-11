#include<iostream>
#include<stack>

using namespace std;

int main(){

	int timeTaken[5]={1,2,4,5,7};

	//if array is not sorted, sort it

	int ary0=timeTaken[0];
	int ary1=timeTaken[1];
	int ary2=timeTaken[2];

	bool dual=(2*ary1)<(ary0+ary2);

	bool ary1onLeft=TRUE;

	int elementsOnLeft=5;
	int elementsOnRight=0;

	while(TRUE){

		if(elementsOnLeft==2){
			moveLeastTwo();
			break;
		}

		moveLeastTwo();
		moveLeastBack();
		moveBiggestTwo();
		moveSecondLeastBack();
	}
}

void moveLeastTwo(){
	elementsOnLeft-=2;
	elementsOnRight+=2;

	timeTaken
}

