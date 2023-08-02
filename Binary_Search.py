//{ Driver Code Starts
//Initial Template for C

#include <stdio.h> 


// } Driver Code Ends
//User function Template for C

int searchInSorted(int arr[], int N, int K) 
{ 
    
       // Your code here
        int L=0;
       int H=N-1;
       int M=L + (H-L)/2;
       
       while(H>=L){
           if(arr[M]==K){
               return 1;
           }
           else if(arr[M]<K){
               L=M+1;
         }else{
           H=M-1;
       }
       M=L + (H-L)/2;
       }
       return -1;
}

//{ Driver Code Starts.


int main(void) 
{ 
    
    int t;
    scanf("%d", &t);
    while(t--){
        int n, k;
        scanf("%d%d", &n, &k);
        
        int arr[n];
        
        for(int i = 0;i<n;i++){
            scanf("%d", &arr[i]);
        }
        
        printf("%d\n", searchInSorted(arr, n, k));

    }

	return 0; 
} 

// } Driver Code Ends
