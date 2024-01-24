abstract class Telephone{
    abstract void lift();
    abstract void disconnected();
}

class SmartTelephone extends Telephone{
    void lift(){
        System.out.println("lift");
    }
    void disconnected(){
        System.out.println("disconnected");
    }
}

public class Assignment1 {
    public static void main(String[] args){
        SmartTelephone myphone = new SmartTelephone();
        myphone.disconnected();
        myphone.lift();
    }
}
