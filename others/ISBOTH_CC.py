x = int(input())
if(x%5==0 and x%11==0):
    print("BOTH")
elif(x%5==0 and x%11!=0):
    print("ONE")
elif(x%5!=0 or x%11==0):
    print("ONE")
else:
    print("NONE")