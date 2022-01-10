
def binary_search_recursion(lst, value, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start > end:
        return None

    mid = (start + end) // 2
    if value == lst[mid]:
        return mid
    if value < lst[mid]:
        return binary_search_recursion(lst, value, start, mid-1)
    if value > lst[mid]:
        return binary_search_recursion(lst, value, mid+1, end)


l = [1, 5, 7, 23, 25, 144]
print(binary_search_recursion(l, 25))
