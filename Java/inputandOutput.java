import java.util.Scanner;
import java.text.NumberFormat;
public class inputandOutput{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter temperature in Farenheit: ");
		int farenheit = input.nextInt();
		System.out.print("Enter day of the week: ");
		//since nextline() only has \n as its delimiter. we cannot use it here since nextInt() is proceeded by \n which nextLine will take as input
		String day = input.next();
		//using nextLine()
		input.nextLine();
		System.out.print("Enter the month and year: ");
		String time = input.nextLine().trim();
		double celsius = 5/9D * (farenheit-32);
		System.out.println("Day: " + day);
		System.out.println("Month and Year: " + time);
		System.out.println("Celsius: " + celsius);
		/*We can remove any leading spaces (and trailing spaces if any) by directly calling the String method trim on the output of nextLine with a statement like this:

		String day = input.nextLine().trim();
*/

		//importing packages: import packageName.memberName;
		//using import packageName.*; imports all members of the packageName package
		
		//formatting with printf
		//printf allows use to use placeholders to print data to the string eg:
		System.out.printf("%s \nCelsius: %f \nFarenheit: %d \n", day, celsius, farenheit);
		/*
		**Decimal (all integers) %d
		**Floating Point (float, double) %f
		**String %s
		**Characters %c
		*/
		// printf does not automatically insert a newline after printing.
		// After the format string parameter, you must enter the actual parameters in the order that printf will use to fill the places held by the format specifiers. 
		//To adjust precision, specify the precision in hte placeholder eg:
		System.out.printf("%.2f\n", celsius);
		//We can also specify the space taken up by the output under printf eg:
		System.out.printf("%10s: %.2f\n", "Celsius", celsius);
		//The space will be placed before any printed character, but to place it after, append a negative sign eg %-10s
		//To add commas to out int values, we can specify it in the placeholder e.g %,lf
		
		//string.format() works the same as printf only that the format is the parameter of the method
		
		//NumberFormat class
		System.out.print("Enter the number of items: ");
		int items = input.nextInt();
		System.out.print("Enter the price per item: ");
		int price = input.nextInt();
		double total = (double)price*items;
		NumberFormat currencyFormat = NumberFormat.getCurrencyInstance();
		System.out.println(currencyFormat.format(total));git
		//DecimalFormat is another class that allows us to format numerical input
		//You create an object then specify the format as the parameter i.e:
		// DecimalFormat formater = new DecimalFormat("0.0");
		// Values are replaced accordingly and they adapt the specified format. # can be used to preserve values to the left of d.p if they are <0
		//if we attatch a % at the end, the number will be multiplied by 100 then it will assume the specified format
	}
}
