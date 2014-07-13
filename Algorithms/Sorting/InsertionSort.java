public class InsertionSort{
	
	public static void main(String args[]){
		
		
		int a[]={2,10,4,7,3,5,12,8,6,9};
		
		System.out.println("Array before sorting : ");
		
		for(int i=0;i<a.length;i++){
			System.out.print(a[i]+" ");
		}
		
		//Sorting starts
		
		for(int i=1;i<a.length;i++){
			int k=i;
			for(int j=i-1;j>=0;j--){				
				if(a[k]<a[j]){
					int temp=a[k];
					a[k]=a[j];
					a[j]=temp;
					k--;
				}
				else{
					break;
				}				
			}			
		}
		
		
		//Sorting ends
		
		
		System.out.println("\n\nArray after sorting : ");
		
		for(int i=0;i<a.length;i++){
			System.out.print(a[i]+" ");
		}
		
	}
	
	
}
