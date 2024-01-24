import java.util.Scanner;
public class ConditionalStatements{
	public static void main(String[] args){
		//I fwe use the equality operator to chek the equality of strings, it will check whether the addresses pointed to by the reference values are the same
		//to actually compare the characters, we use a string method .equals() ie
		String name = ("David");
		String place = ("Ngong");
		System.out.println(name.equals(place));  // Returns false
		//string interns i where java creates a pull of strings once you create a string object. It then checks if another reference value points to a value already existing in the pull and if it does, it doesn't create a new objext, instead, it makes the two alieses
		//toCompare()
		//compares the values of two strings index by index and has three return values
		//say name.toCompare(place)
		/*
		** >0 if name>place
		** 0 if name==place
		** <0 if name<place
		*/
		
		//Note that relational operators have higher precedence than logical operators
		//AND takes precedence over OR.
		//Not (!) takes precedence over AND and OR.
		//Parentheses take precedence over logical operators.
		//This process of skipping the right-sided operand based on the result of the left-sided operand is called short-circuit evaluation.
		//Else matches to its nearest if
		//Tenary operator: condition ? expression1 : expression2
		//consecutive if statements means the second is nested within the first
	}
}
