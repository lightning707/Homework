def merge_sort(li):
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]
        right = li[mid:]

        merge_sort(left)
        merge_sort(right)

        ind_left = 0
        ind_right = 0

        ind_iter = 0

        while ind_left < len(left) and ind_right < len(right):
            if left[ind_left] <= right[ind_right]:
                li[ind_iter] = left[ind_left]
                ind_left += 1
            else:
                li[ind_iter] = right[ind_right]
                ind_right += 1
            ind_iter += 1

        while ind_left < len(left):
            li[ind_iter] = left[ind_left]
            ind_left += 1
            ind_iter += 1

        while ind_right < len(right):
            li[ind_iter] = right[ind_right]
            ind_right += 1
            ind_iter += 1


lst = [5, 10, 4, 2, 3, 15, 1]
merge_sort(lst)
print(lst)
