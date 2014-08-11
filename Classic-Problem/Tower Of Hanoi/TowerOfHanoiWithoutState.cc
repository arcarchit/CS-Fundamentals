#include<iostream>

using namespace std;

void towers(int noOfDisk, char fromTower, char toTower, char mediator);

int main(){
	
	int noOfDisks;
	cout<<"Welcome, Please enter no of disks : ";
	cin>>noOfDisks;

	towers(noOfDisks,'A', 'B', 'C');
	return 0;
}

void towers(int noOfDisk, char fromTower, char toTower, char mediator){

	if(noOfDisk==1){
		cout<<"Move Disk "<<noOfDisk<<" from tower "<<fromTower<<" to "<<toTower<<endl;
		return;
	}

	towers(noOfDisk-1,fromTower, mediator, toTower);
	cout<<"Move Disk "<<noOfDisk<<" from tower "<<fromTower<<" to "<<toTower<<endl;
	towers(noOfDisk-1,mediator, toTower, fromTower);
}
