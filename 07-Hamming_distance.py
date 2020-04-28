#hamming distance

def hammingDistance(n1,n2):
    x=n1^n2
    c=0
  
    while x>0: 
        c+=x&1
        x>>=1
      
    return c