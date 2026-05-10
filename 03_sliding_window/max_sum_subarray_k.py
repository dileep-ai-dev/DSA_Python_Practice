def max_sum_subarray(arr, k):
    left = 0
    window_sum = 0
    max_sum = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[left]
            left += 1

    return max_sum


arr = [2, 1, 5, 1, 3, 9]
k = 3
print(max_sum_subarray(arr, k))