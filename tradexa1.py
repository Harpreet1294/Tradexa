def rotate(arr,num):
    out=[]
    for item in range(len(arr)-num,len(arr)):
        out.append(arr[item])
    for item in range(0,len(arr)-num):
        out.append(arr[item])
    return out;
arr=[]
num=int(input())
n=int(input("Enter number of elements"))
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
print(rotate(arr,num));

    
