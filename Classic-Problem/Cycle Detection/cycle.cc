#include <iostream>

using namespace std;

class Node{

	public:

	int value;
	Node* next;

	Node(int a, Node* nextL){
		value=a;
		next=nextL;
	}

	Node(int a){
		value=a;
	}

};

bool checkForCycle(Node* firstNode){

	Node *tortoise, *hare;
	tortoise=firstNode;
	hare=firstNode;

	while(hare && hare->next && tortoise){
		tortoise=tortoise->next;
		hare=hare->next->next;

		if(tortoise==hare)
			return true;
	}

	return false;
}

void detectFaultyNode(Node* firstNode){

	Node *tortoise, *hare;
	tortoise=firstNode;
	hare=firstNode;

	while(hare && hare->next && tortoise){
		tortoise=tortoise->next;
		hare=hare->next->next;

		if(tortoise==hare)
			break;
	}

	tortoise=firstNode;

	while(tortoise!=hare){
		tortoise=tortoise->next;
		hare=hare->next;
	}
	int val=hare->value;
	cout<<"Faulty Node Value : "<<val<<endl<<endl;

}



int main(){


	Node last(2, 0);
	Node a(3, &last);
	Node b(4, &a);
	Node c(5, &b);
	Node d(6,&c);

	a.next=&c;

	Node* currentNode=&d;

//	bool checkCycle=checkForCycle(currentNode);
	detectFaultyNode(currentNode);

//	cout<<checkCycle<<endl<<endl;

	int iteration=0;

	while (currentNode){
		int temp=(currentNode->value);
		cout<<temp<<endl;
		currentNode=currentNode->next;

		if(iteration++==10)
			break;
	}

	return 0;
}
