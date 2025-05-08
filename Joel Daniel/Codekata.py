#%%
def tribonacci(signature, n, steps=0):
    x = sum(signature[-3:])
    if n < 4:
        return signature[:n] 
    if steps == n - 3:
        return signature
    return tribonacci(signature + [x], n ,steps + 1) 

tribonacci([1,1,1],10)


#%%
def dir_reduc(arr):
    opposite = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    i = 0
    while i < len(arr) -1: 

        if arr[i]==opposite[arr[i+1]]:
            print (arr,i)
            del arr[i+1]
            del arr[i]
            if i!=0:
                i-=1
        else:
            i+=1
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dir_reduc(a)