#include<iostream>
#include<stack>

using namespace std;

void towers(int diskNo, char fromTower, char toTower, char mediator);
showStatus();

stack<int> fromToMediator[3];

int main(){

	int noOfDisks;
	cout<<"Enter number of disks : ";
	cin>>noOfDisks;
	int temp=noOfDisks;

	while(temp>0)
		fromToMediator[0].push(temp--);

	towers(noOfDisks, 'A', 'B', 'C');

	return 0;
}


void towers(int diskNo, char fromTower, char toTower, char mediator){

	if(diskNo==0)
		return;

	towers(diskNo-1, fromTower, mediator, toTower);
	cout<<"Move "<<diskNo<<" from tower "<<fromTower<<" to "<<toTower<<endl;

	int temp=fromToMediator[(int)fromTower-65].top();
	fromToMediator[(int)fromTower-65].top();
	fromToMediator[(int)toTower-65].push(temp);

	showStatus();

	cout<<"Element Popped Out is : "<<temp;
	towers(diskNo-1, mediator, toTower, fromTower);
}

showStatus(){

cout<<"Disks in tower A are : ";


}
