import java.util.logging.Level;

public class Classes{
    public static void main(String[] args) {
        Car mycar = new Car();
        mycar.setModel("Toyota");
        System.out.println(mycar.getModel());
        mycar.hoot();
        Vehicle myvehicle = new Vehicle();
        myvehicle.hoot();
        OuterClass myClass = new OuterClass();
        OuterClass.InnerClass innerClass = myClass.new InnerClass();// accessing the inner class
        Dog myDog = new Dog();
        myDog.animalSound();
        System.out.println(mycar.mylevel);

    }
}

class Vehicle{
    public void hoot(){
        System.out.println("Pee pee");
    }

    enum Levels{
    LOW,
    MEDIUM,
    HARD
}
}
class Car extends Vehicle{
    private int makeYear;
    private String model;

    //getter
    public String getModel(){
        return model;
    }

    //setter
    public void setModel(String make){
        this.model = make;
    }

    //polymorphism
    public void hoot(){
        System.out.println("Pop pop");
    }

    Levels mylevel = Levels.LOW;
}

class OuterClass{
    int x = 5;
    class InnerClass {
        int y = 5;
    }
}

interface Animal{
    public void animalSound();
    public void animalType();
}

abstract class Mammal{
    public boolean mammaryGlands = true;
    abstract void mammalFunction();
}



class Dog extends Mammal implements Animal {
    public void animalSound(){
        System.out.println("A dog goes Woof");
    }
    public void animalType(){
        System.out.println("This is a dog");
    }

public void mammalFunction(){
    System.out.println("A dog is a mammal");
}
}

