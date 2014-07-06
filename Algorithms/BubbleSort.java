public class BubbleSort{
	
	public static void main(String args[]){
				
		int a[]={2,10,4,7,3,5,12,8,6,9};
		
		System.out.println("Array before sorting : ");
		
		for(int i=0;i<a.length;i++){
			System.out.print(a[i]+" ");
		}
		
		for(int i=0;i<a.length;i++){
			for(int j=i+1;j<a.length;j++){
				if(a[i]>a[j]){
					int temp=a[i];
					a[i]=a[j];
					a[j]=temp;
				}
			}//inner 			
		}//outer
		
		System.out.println("\n\nArray after sorting : ");
		
		for(int i=0;i<a.length;i++){
			System.out.print(a[i]+" ");
		}
	}
	
}
