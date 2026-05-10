def pair_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return left, right
        elif s < target:
            left += 1
        else:
            right -= 1

    return -1, -1


arr = [6, 7, 8, 9, 10]
target = 18
print(pair_sum(arr, target))