#include<iostream>
#include<cmath>
#include<cstdlib>
#include<stdio.h>

#define N 5
#define M 6
#define GOAL 30

using namespace std;

int goal;
int visited=0;
int chessBoard[N][M];
int i=0,j=0;

void solve(int currentI, int currentJ);
void getNextMove(int moves,int* nextI,int* nextJ);
void printArray();

int main(){

	cout<<"Starting the program : "<<endl;

	int m,n;
	

	for(n=0;n<N;n++){
		for(m=0;m<M;m++){
			chessBoard[n][m]=-1;
		}
	}

	solve(0,0);


	cout<<"Program completes. Visted = "<<visited<<endl;
	printArray();
	
}

void solve(int currentI, int currentJ){

	if(currentI>(N-1) || currentI<0 || currentJ>(M-1) || currentJ<0)
		return;

	if(chessBoard[currentI][currentJ]!=-1)
		return;

	chessBoard[currentI][currentJ]=++visited;


	if(visited==GOAL){
		printArray();
		exit(0);
		cout<<endl<<"**************************************"<<endl;
	}

	int moves=0;

	for(moves=0;moves<8;moves++){
		int nextI=currentI;
		int nextJ=currentJ;
		getNextMove(moves, &nextI, &nextJ);
		solve(nextI, nextJ);
	}
	chessBoard[currentI][currentJ]=-1;
	visited--;
}

void getNextMove(int moves,int* nextI,int* nextJ){

	switch (moves) {
		case  0:
			*nextI+=2;
			*nextJ+=1;
			break;
		case  1:
			*nextI+=2;
			*nextJ+=-1;
			break;
		case  2:
			*nextI+=-2;
			*nextJ+=1;
			break;
		case  3:
			*nextI+=-2;
			*nextJ+=-1;
			break;
		case  4:
			*nextI+=1;
			*nextJ+=2;
			break;
		case  5:
			*nextI+=-1;
			*nextJ+=2;
			break;
		case  6:
			*nextI+=1;
			*nextJ+=-2;
			break;
		case  7:
			*nextI+=-1;
			*nextJ+=-2;
			break;
	}
}


void printArray(){
	int m,n;
	cout<<endl;
	for(n=0;n<N;n++){
		for(m=0;m<M;m++){
			printf("%2d\t",chessBoard[n][m]);
		}
	cout<<endl<<endl<<endl;
	}
}
