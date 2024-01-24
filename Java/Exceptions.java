
public class Exceptions {
    static void divisonCheck(int num1, int num2){
            if(num2 == 0){
                throw new ArithmeticException("Cannot divide by 0");
            }else{
                double quotient = (double)num1/num2;
                System.out.println(quotient);
            }
            
        
    }
    public static void main(String[] args) {
        divisonCheck(150, 0);
    }
}
