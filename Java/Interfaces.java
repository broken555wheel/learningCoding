abstract class Animal{
	abstract void SleepingSound();
}
class Pig extends Animal{
    void SleepingSound(){
        System.out.println("zzz");
    }
    public void AnimalSound(){
        System.out.println("wee wee");
    }
}

class Interfaces{
    public static void main(String[] argz){
       Pig mypig = new Pig();
       mypig.SleepingSound();
       mypig.AnimalSound(); 
    }
}
