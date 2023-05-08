def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_desc(left)
    right = merge_sort_desc(right)

    return merge_desc(left, right)


def merge_desc(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result[::-1]

lst1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
lst2 = [20,21,22,23,24,25,26,27]
lst3 = [30,29,31,33,19,20,31,21,59]
print(merge_sort_desc(lst1))
print(merge_sort_desc(lst2))
print(merge_sort_desc(lst3))

[2000, 129, 59, 56, 24, 19, 12, 10, 9, 8, 7, 6, 6, 5, 4, 3, 3, 2, 1, 1]
[27, 26, 25, 24, 23, 22, 21, 20]
[33, 31, 31, 30, 29, 21, 20, 19, 59]