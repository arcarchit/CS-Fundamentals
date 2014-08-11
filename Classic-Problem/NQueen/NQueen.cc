#include<iostream>

using namespace std;

int N;
void printSquare(int* ans);
void getAns(int* ans);
void recursiveCall(int* ans, int currentPosition);

int main(){

	cout<<"Enter Vaule of N ";
	cin>>N;

	int ans[N];

	getAns(ans);

	return 0;
}


bool checkAns(int* ans, int currentPosition){
	for(int i=0;i<currentPosition;i++){
		if(ans[i]==ans[currentPosition])
			return false;
		if((i-currentPosition)==(ans[i]-ans[currentPosition]))
			return false;
		if((currentPosition-i)==(ans[i]-ans[currentPosition]))
			return false;
	}
	return true;
}


void getAns(int* ans){
	recursiveCall(ans, 0);
}

void recursiveCall(int* ans, int currentPosition){

	if(currentPosition==N){
		printSquare(ans);
	}
	else{
	for(int i=0;i<N;i++){
		ans[currentPosition]=i;
		if(checkAns(ans, currentPosition)){
			recursiveCall(ans,currentPosition+1);
		}
	}
	}

}

void printSquare(int* ans){

	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(i==ans[j])
				cout<<"Q ";
			else
				cout<<"* ";
		}
		cout<<endl;
	}
	cout<<endl<<endl;
}
