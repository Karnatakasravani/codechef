#User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        
        import math
        # code here 
        a=[]
        m=int(math.sqrt(N))
		for i in range(1,m+1):
		    k=N//i
    		if k*i==N:
                a.append(k)
                a.append(i)
        if N!=1:
            a.remove(N)
		l=sum(a)
		if l==N:
		    return 1
		return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends
