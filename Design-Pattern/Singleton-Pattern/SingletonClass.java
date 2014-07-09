public class SingletonClass{
	
	private static SingletonClass object=new SingletonClass();
	
	private SingletonClass(){};
	
	public static SingletonClass getInstance(){
		return object;
	}
	
	public void doStuff(){
		System.out.println("Utility Stuff goes here");
	}
			
}
