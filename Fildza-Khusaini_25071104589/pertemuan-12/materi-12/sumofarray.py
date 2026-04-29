# Function to calculate the sum of an array recursively

def RecSum(arr, n):
    if n <= 0:
        return 0
    return RecSum(arr, n - 1) + arr[n - 1]


def arraysum(arr):
    return RecSum(arr, len(arr))

# Driver code
arr = [1, 2, 3, 4, 5]
print(arraysum(arr))