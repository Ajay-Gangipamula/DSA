def mergesort(arr,i,j,count):
	if(i>=j):
		return
	m=i+(j-i)//2
	mergesort(arr,i,m,count)
	mergesort(arr,m+1,j,count)
	merge(arr,i,m,m+1,j,count)

def merge(arr,s1,e1,s2,e2,count):
	i=s1
	j=s2
	temp=[]
	while(i<=e1 and j<=e2):
		if(arr[i][0]>arr[j][0]):
		    count[arr[i][1]]+=e2-j+1
		    temp.append(arr[i])
		    i+=1
		else:
			temp.append(arr[j])
			j+=1
	while(i<=e1):
		temp.append(arr[i])
		i+=1
	while(j<=e2):
		temp.append(arr[j])
		j+=1
	k=0
	for i in range(s1,e2+1):
		arr[i]=temp[k]
		k+=1

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr=[]
        n=len(nums)
        for i in range(n):
            arr.append([nums[i],i])
        count=[0]*n
        mergesort(arr,0,n-1,count)
        return count