public class ArrayLesson{
	public static void main(String[] args){
		//declaration
		//dataType[] identifier = new dataType[arraylLength];
		//elements in an array are reference variables
		//default value for boolean arrays is false while that of object arrays is null
		double[] weekHighs = {80, 70, 69, 72, 74, 90};
		double sum = 0D;  //Values must be initialzed before usage in the array
		double average = 0D;
		for(int i = 0; i < weekHighs.length; i++){
			sum+=weekHighs[i];
		}
		average = sum/weekHighs.length;
		System.out.printf("The average teperature for the week was %.2f\n", average);
		//for each statement scan be used to iterate arrays
		//for(sameDataType : arrayName){}
		for(double temp : weekHighs){
			System.out.println(temp);
			
		}
		//A null reference does not point to an actual object. We, therefore,  cannot legally use it to invoke a method
		//Double.parsedouble(varName) - converts to double
		
		//2d arrays
		//declaration
		//dataType[][] identifier = {{},{}}; (when initializing)
		//dataType[][] identifier = new dataType[rows][columns]
		//traversing
		//outer loop - array.length;row++, inner loop - array[rows].length;column++
		//ragged arrays have different number of columns per row. 
	}
}
