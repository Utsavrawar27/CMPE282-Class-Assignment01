import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    i=1
    res=0
    while True:
        if i==len(arr)-1:
            break
        for j in range(i+1,len(arr)+1):
            temp=arr[i-1:j]
            if (arr[i-1]*arr[j-1])<=max(temp):
                res+=1
        i+=1        
    return res 

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    print(result)