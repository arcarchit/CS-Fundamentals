public class SelectionSort{
	
	
	public static void main(String args[]){
		
				
		int a[]={2,10,4,7,3,5,12,8,6,9};
		
		System.out.println("Array before sorting : ");
		
		for(int i=0;i<a.length;i++){
			System.out.print(a[i]+" ");
		}
		
		//Sorting starts


		for(int i=0;i<a.length;i++){
			int min=a[i];
			int minIndex=i;
			
			for(int j=i+1;j<a.length;j++){
				if(a[j]<min){
					min=a[j];
					minIndex=j;
				}				
			}
			
			int temp=a[i];
			a[i]=a[minIndex];
			a[minIndex]=temp;
					
		}

		//Sorting ends
		
		
		System.out.println("\n\nArray after sorting : ");
		
		for(int i=0;i<a.length;i++){
			System.out.print(a[i]+" ");
		}

	}

}
