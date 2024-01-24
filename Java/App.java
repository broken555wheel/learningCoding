interface Sounds{
	void AnimalSound();
	void SleepingSound();
}

class Animal implements Sounds{
	public void AnimalSound(){
		System.out.println("barks");
	}
		
	public void SleepingSound(){
		System.out.println("zzz");
	}
}
class App{

	public static void main(String[] args){
		Animal myanimal = new Animal();
		myanimal.AnimalSound();
	}
}


