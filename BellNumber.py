#bell numbers
#amazon
#find nth bell number , pyramid method

n = 5
arr = [[0 for i in range(n+1)] for j in range(n+1)]
arr[0][0] = 1
for i in range(1,n+1):
    for j in range(0,i+1):
        if(j==0):
            arr[i][j] = arr[i-1][i-1]
        else:
            arr[i][j] = arr[i][j-1] + arr[i-1][j-1]
for i in range(0,n+1):
    print("Bell number for "+str(i)+" is "+str(arr[i][0]))
        
        