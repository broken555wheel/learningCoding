import java.util.Scanner;
public class FarenheittoCelcius{
	public static void main(String[] args){
		//Scanner is the class in the API that we use to read user input
		//Each method for reading and returning data is prefixed with the word “next”.
		/*
		**The nextInt and nextDouble methods read individual tokens and return them as ints and doubles respectively. 
		**The next() method reads a token and returns it as a String value.  
		**The nextLine()returns a String, but it keeps pulling characters from the stream until it reaches a new line character. 
		**Tokens are determined by where the delimiters appear. Delimiters are often whitespace except fot nextLine() where the delimiter is only \n
		*/
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a Farenheit value: ");
		int farenheit = input.nextInt();
		double celcius = 5D/9 * (farenheit-32);
		System.out.println("Celcius: "+celcius);
		//the nextInt method skips any leading whitespace when scanning for tokens.  This rule, in fact, applies to all Scanner next methods except nextLine, which includes them in the returned String
		
		//Scannner errors
		//errors will be returned if the data entered is not supported by the next()method
		
		
	}
}

i
