
public class Permutations{

	private static int MAX_POSITION;
	static char[] ary={'a','b','c','d'};

	public static void main(String[] args) {

		MAX_POSITION=ary.length-1;

		permute(0);


	}

	static void permute(int position){

		if(position==MAX_POSITION){
			printAll();
		}
		else{
			for(int j=position;j<=MAX_POSITION;j++){
				swap(position, j);
				permute(position+1);
				swap(position, j);
			}


		}

	}

	static void printAll(){
		for(int i=0;i<=MAX_POSITION;i++){
			System.out.print(ary[i]);
		}
		System.out.println();
	}
	
	static void swap(int positionI, int positionJ){
		char temp=ary[positionI];
		ary[positionI]=ary[positionJ];
		ary[positionJ]=temp;		
	}
	
}
