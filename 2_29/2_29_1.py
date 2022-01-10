def bubble_sort_double(li):
    len_ = len(li)
    swapped = True
    start = 0
    end = len_ - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                swapped = True

        if not swapped:
            break
        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]

        start = start + 1
    return li


print(bubble_sort_double([15, 7, 2, 10, 5]))
