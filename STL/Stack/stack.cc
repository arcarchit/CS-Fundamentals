#include<iostream>
#include<stack>

using namespace std;

int main(){
	

	stack<int> myStack;

	for(int i=0;i<5;i++)
		myStack.push(i);
	cout<<"Popping out animal "<<endl;

	while(!myStack.empty()){
		cout<<myStack.top()<<endl;
		myStack.pop();
	}


}
