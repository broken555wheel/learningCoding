import java.util.Scanner;
public class StringExercise{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int[] numarray = new int[10];
		for(int i=0;i<numarray.length;i++){
			System.out.printf("Enter number %d: ", i+1);
			numarray[i] = input.nextInt();
		}
		
		for (int j=0;j<numarray.length;j++){
			for (int k=0; k<numarray.length-1-j;k++){
				int placeholder = 0;
				if (numarray[k]>numarray[k+1]){
					placeholder = numarray[k+1];
					numarray[k+1] = numarray[k];
					numarray[k] = placeholder;
				}
			}
			
			
		}
		for(int number: numarray){
			System.out.println(number);
		}

	}
}
