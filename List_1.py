# Reverse a list without using built-in function

# Method 1:
original=[1,2,3,4,5]
rev=[]
for i in range(len(original)-1,-1,-1):
    rev.append(original[i])
print(rev)

# Method 2:
lst=[1,2,3,4,5]
start=0
end=len(lst)-1
while start<end:
    lst[start],lst[end]=lst[end],lst[start]
    start+=1
    end-=1
print(lst)