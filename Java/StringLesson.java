public class StringLesson{
	public static void main(String[] args){
		String major;
		major = new String("Computer Science");
		// String major = new String("Computer Science")
		// String major = ("Computer Science"); (Mostly for the strings though)
		int stringLength = major.length();
		System.out.println(stringLength);
		String playerOne = "Alex";
		String playerTwo = "Kathy";
		playerTwo = playerOne;

		int lengthOne = playerOne.length();
		int lengthTwo = playerTwo.length();

		System.out.println(lengthOne + " " + lengthTwo);
		//Output will be 4 4 since both player one and player two point to Alex, with player two pointing to its address, but still being able to access and manipulate it
		
		//Examples of String Methods
		//toLowerCase - returns the srting in lowercase
		String interest = new String("Taking long walks on the Beach");
		System.out.println(interest.toLowerCase());
		//concat() concatenates two srtings
		System.out.println(major.concat(interest));  //Same as major+interest
		//replace(char, char) replaces the first chars with the second
		String interests = ("Computer Science, Long Walks on the Beach");
		System.out.println(interests.replace(" ","!"));
		//substring() returns a new string geerated by copying the characters between the specified indices
		//The copying is done from the beginning index to just before the ending one
		System.out.println(interests.substring(0,5));
		//The compiler does not check the length of our string so it is possible to encounter a runtime error if we reference an invalid string index
		//The max we can reference is string length + 1
		
		//indexOf(string) 
		//returns the index of the first occurrence of the sequence of characters within its parameters else returns -1
		System.out.println(interests.indexOf("Ca")); //returns -1
		//also returns the index of the character whose unicode is represented in the parameters
		System.out.println(interests.indexOf('a'));
		//The mothods above do not mutate the string
		}
}
