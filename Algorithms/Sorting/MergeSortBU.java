/*
This is BU (Bottom-Up) implementation of merge sort.
It is non recursive, using looping instead of recusion.
Because of this fact it is somewhta faster than Top-Down approach.
*/
public class MergeSortBU{

	private static int[] numbers={2,10,4,7,3,5,12,8,1,6,3};

	private static int[] helper;

	public static void main(String args[]){


		System.out.println("Array before sorting : ");

		for(int i=0;i<numbers.length;i++){
			System.out.print(numbers[i]+" ");
		}

		//Sorting starts

		sort();

		//Sorting ends


		System.out.println("\n\nArray after sorting : ");

		for(int i=0;i<numbers.length;i++){
			System.out.print(numbers[i]+" ");
		}

		System.out.println();

	}

	public static void sort(){
		int length=numbers.length;
		helper=new int[length];

		for(int level=1;level<length;level=level+level){
			for(int i=0;i<length-level;i+=level+level){
				int low=i;
				int mid=low+level-1;
				int high=Math.min(low+level+level-1,length-1);
				merge(low, mid, high);
			}
		}
	}


	public static void merge(int low, int middle, int high){
		for(int i=low;i<=high;i++){
			helper[i]=numbers[i];
		}

		int lower=low;
		int upper=middle+1;

		for(int index=low;index<=high;index++){
			if(lower>middle)	numbers[index]=helper[upper++];
			else if (upper>high)	numbers[index]=helper[lower++];
			else  if(helper[upper]<helper[lower])	numbers[index]=helper[upper++];
			else numbers[index]=helper[lower++];
		}

	}
}
