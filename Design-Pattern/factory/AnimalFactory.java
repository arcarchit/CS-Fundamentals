public class AnimalFactory{

		public static Animal getAnimal(String input){
			
			if(input==null){
				return null;
			}
			
			if(input.equals("Cat")){
				return new Cat();
			}
			
			if(input.equals("Dog")){
				return new Dog();
			}
			
			if(input.equals("Lion")){
				return new Lion();
			}
			
			return null;
			
		}	
}
