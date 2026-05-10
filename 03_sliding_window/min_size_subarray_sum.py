def min_subarray_len(arr, target):
    left = 0
    window_sum = 0
    min_len = float("inf")

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1

    if min_len == float("inf"):
        return 0
    return min_len


arr = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len(arr, target))