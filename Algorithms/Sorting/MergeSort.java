public class MergeSort{

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
		int low=0;
		int high=numbers.length-1;
		helper=new int[high+1];
		mergeSort(low, high);
	}

	public static void mergeSort(int low, int high){
		if(low>=high){
			return;
		}
		int middle=low+(high-low)/2;
		mergeSort(low,middle);
		mergeSort(middle+1, high);
		merge(low, middle, high);
	}

	public static void merge(int low, int middle, int high){
		for(int i=low;i<=high;i++){
			helper[i]=numbers[i];
		}

		int index=low;	
		int lower=low;
		int upper=middle+1;
		while(lower<=middle && upper<=high){
			if(helper[lower]<helper[upper]){
				numbers[index++]=helper[lower++];
			}
			else{
				numbers[index++]=helper[upper++];
			}
		}
		while(lower<=middle){
			numbers[index++]=helper[lower++];
		}
	}
}
