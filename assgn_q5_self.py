sp=0
st=75

for i in range(1,7):
    for j in range(0,sp):
        print(" ", end="")
    for k in range(65,st+1):
        print(chr(k),end=" ")  
    
    
    print()
    sp+=2
    st-=2
