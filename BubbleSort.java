package sorting;

public class BubbleSort {
	void bubblesort(int arr[])
	{
		int n =arr.length;
		for(int i=0;i<n-1;i++)
			for(int j=0;j<n-i-1;j++)
				if(arr[j] > arr[j+1])
				{
					int temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
					
				}
					
		}
	void printArray(int arr[])
	{
		int n=arr.length;
		for(int i=0;i<n;i++)
			System.out.printf(" "+arr[i]);
		System.out.println();
		}
	public static void main(String []args) {
		BubbleSort bs=new BubbleSort();
		int arr[]= {78,1,45,2,85,12,122,4,10,0};
		bs.bubblesort(arr);
		System.out.println("Array Sort");
		bs.printArray(arr);
	}

}
