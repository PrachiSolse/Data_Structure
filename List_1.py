# Reverse a list without using built-in function

# Method 1:
original=[1,2,3,4,5]
rev=[]
for i in range(len(original)-1,-1,-1):
    rev.append(original[i])
print(rev)