# Program to determine min. no of edits to transform str1 to str2.
# operattions are either insert, remove or modify.

def editDistance(str1,str2,m,n):
    if m==0: 
         return n 
    if n==0: 
        return m 
  
    if str1[m-1]==str2[n-1]: 
        return editDistance(str1,str2,m-1,n-1) 
   
    return 1+min(editDistance(str1,str2,m,n-1),    
                 editDistance(str1,str2,m-1,n),    
                 editDistance(str1,str2,m-1,n-1)) 

x="MOVIE"
y="LOVE"
n=len(x)
m=len(y)

print(editDistance(x,y,n,m)) 