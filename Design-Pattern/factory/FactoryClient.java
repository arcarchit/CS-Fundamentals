public class FactoryClient{
	
	public static void main(String args[]){
		
		Animal a=AnimalFactory.getAnimal("Cat");
		if(a==null)
			System.out.println("Animal factory returned null");
		a.makeSound();
		
		a=AnimalFactory.getAnimal("Dog");
		if(a==null)
			System.out.println("Animal factory returned null");
		a.makeSound();
		
		a=AnimalFactory.getAnimal("Cat");
		if(a==null)
			System.out.println("Animal factory returned null");
		a.makeSound();
	}
	
}
