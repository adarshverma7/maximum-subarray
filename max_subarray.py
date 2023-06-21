def sub_array(arr):
    n=len(arr)
    max_sum=float('-inf')
    start_index=0
    end_index=0
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum+=arr[j]
            if max_sum<current_sum:
                max_sum=current_sum
                start_index=i
                end_index=j
    subarray=arr[start_index : end_index+1]
    return max_sum, subarray
arr=[10,5,-2,4,0]
max_sum, subarray=sub_array(arr)
print(max_sum)
print(subarray)