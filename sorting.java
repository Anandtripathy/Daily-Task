package sorting;
import java.util.Arrays;
import java.util.Collections;
public class sorting {
	public static void main (String[] args)
	{
		Integer arr[] = {13,7,4,5,1,10,2,14,3,101,102};
		{
		Arrays.sort(arr);
		System.out.printf("Modifed Arrays: %s", Arrays.toString(arr) );
		}
		{
		Arrays.sort(arr, Collections.reverseOrder());
		System.out.printf("\n Modifed Arrays: %s", Arrays.toString(arr) );
			}

}
}
