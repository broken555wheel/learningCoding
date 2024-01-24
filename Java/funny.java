import java.util.Scanner;
public class funny {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = input.nextLine().trim();
        System.out.print("Enter your age: ");
        int age = input.nextInt();
        System.out.print("Enter your occupation:");
        String job = input.next();
        input.nextLine();
        System.out.printf("Hello %s, Nice to meet you.\n You are %d years old and you are a %s.\n", name, age, job);
    }
}
