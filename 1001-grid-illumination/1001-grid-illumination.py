class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row,col,major,minor={},{},{},{}
        visited={}
        for i in range(len(lamps)):
            i1,j1=lamps[i][0],lamps[i][1]
            if (i1,j1) not in visited:
                if i1 in row:
                    row[i1]+=1
                else:
                    row[i1]=1
                if j1 in col:
                    col[j1]+=1
                else:
                    col[j1]=1
                if (i1-j1) in major:
                    major[i1-j1]+=1
                else:
                    major[i1-j1]=1
                if (i1+j1) in minor:
                    minor[i1+j1]+=1
                else:
                    minor[i1+j1]=1
                visited[(i1,j1)]=1
        ans=[]
        for q in queries:
            x=q[0]
            y=q[1]
            x1,y1,x2,y2=0,0,0,0
            if x in row:
                x1=row[x]
            if y in col:
                y1=col[y]
            if x-y in major:
                x2=major[x-y]
            if x+y in minor:
                y2=minor[x+y]
            if(x1>0 or y1>0 or x2>0 or y2>0):
                ans.append(1)
                for i in range(-1,2):
                    for j in range(-1,2):
                        a=x+i
                        b=y+j
                        if(a>=0 and a<n and b>=0 and b<n and ((a,b) in visited)):
                            if a in row:
                                row[a]-=1
                            if b in col:
                                col[b]-=1
                            if a-b in major:
                                major[a-b]-=1
                            if a+b in minor:
                                minor[a+b]-=1
                            del visited[(a,b)]
            else:
                ans.append(0)
        return ans