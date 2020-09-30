package sorting;

public class MergeSort {
	void mergesort(int arr[]) {
	int n=arr.length;
	for(int i=0;i<n-1;i++)
		for(int j=0;j<n-i-1;j++)
			if(arr[j]> arr[j+1])
			{
				int temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
				
			}

	int l=arr.length;
	for(a=0;a<l-1;a++)
		for(b=0;b<)
}
