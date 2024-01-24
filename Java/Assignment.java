interface BasicAnimal{
    void eat();
    void sleep();
}


class Monkey{
    public void jump(){
        System.out.println("jump");
    }
    public void bite(){
        System.out.println("bite");
    }
}

class Human extends Monkey implements BasicAnimal{
    public void eat(){
        System.out.println("eat");
    }
    public void sleep(){
        System.out.println("sleep");
    }
}
public class Assignment {
    public static void main(String[] args){
        Human newHuman = new Human();
        newHuman.eat();
        newHuman.sleep();
        newHuman.jump();
        newHuman.bite();
    }
}