#include<iostream>
#include<stack>

using namespace std;

int noOfCities;
int matrix[10][10];

void tsp();

int main(){

cout<<"Enter No Of Cities : ";
cin>>noOfCities;


cout<<"Enter Adjacecncy matrix :"<<endl;

for(int i=0;i<noOfCities;i++){
	for(int j=0;j<noOfCities;j++){
		cin>>matrix[i][j];
	}
}

cout<<endl<<endl<<"Outputting Entered matrix"<<endl<<endl;

for(int i=0;i<noOfCities;i++){
	for(int j=0;j<noOfCities;j++){
		cout<<matrix[i][j]<<" ";
	}
	cout<<endl;
}

tsp();

return 0;

}


/***************************************************************/


void tsp(){

	cout<<"Sequence for cities to be visited are : "<<endl;

	int visited[10]={0,0,0,0,0,0,0,0,0,0};

	stack<int> cityStack;
	cityStack.push(0);

	int noOfVisitedCities=0;

//	cout<<currentCity<<" ";

	while(!cityStack.empty()){

		int currentCity=cityStack.top();
		visited[currentCity]=1;
		cout<<currentCity<<" ";
		noOfVisitedCities++;

		if(noOfVisitedCities==10){
			cout<<endl;
			return;
		}

		//Find nearest non visited city from currentCity
		int min=10000;
		int nextCity;
		for(int i=0;i<10;i++){
			if(!visited[i]){
				if(min>matrix[currentCity][i]){
					min=matrix[currentCity][i];
					nextCity=i;
			}
		}
		cityStack.push(nextCity);
	}




	}
}

