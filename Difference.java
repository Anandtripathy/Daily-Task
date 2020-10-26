import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;


class Difference {
  	private int[] elements;
  	public int maximumDifference;
      int max = 1; 
       int min = 100;
        for(int element : elements){
        if(element < min){
            min = element;
        }
        if(element > max){
            max = element;
        }
    }
        
    this.maximumDifference = Math.abs(max - min);
}

	// Add your code here

} // End of Difference class

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}