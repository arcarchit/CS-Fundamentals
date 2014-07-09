public class SingletonClient{
	
	public static void main(String args[]){
		
		SingletonClass instance=SingletonClass.getInstance();		
		instance.doStuff();
	}
	
}
