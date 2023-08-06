class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer=[0]*len(queries)
        allxor=[0]*len(arr)
        allxor[0]=arr[0]
        for i in range(len(arr)-1):
            allxor[i+1]=(arr[i+1]^allxor[i])
        for j in range(len(queries)):
            if(queries[j][0]!=0):
                answer[j]=(allxor[queries[j][1]]^allxor[queries[j][0]-1])
            else:
                answer[j]=(allxor[queries[j][1]])
        return answer