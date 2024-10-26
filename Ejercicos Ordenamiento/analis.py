arr=[-2,11,-4, 13,-5,-2]

def sumatoria(arr):
    sum=0
    for i in range(1,len(arr)):
        if(i==4):
            break
        else:
            sum+=arr[i]
    return sum

print(sumatoria(arr))


def sumatoria2(arr):
    sum=0   #   1
    i=1     #   1
    while i<=len(arr): #n
        if(i==4):       #n
            break
        else:
            sum += arr[i] #n
            i+=1        #n
    return sum
print(sumatoria2(arr))









