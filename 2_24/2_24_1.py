from typing import List, Tuple

# We assume that all lists passed to functions are same length N
# answers
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n


# O(1 + N + log N) = O(N)
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


# O(10 * 1) = O(1)
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


# O(1 + N * N + 1) = O(N^2)
def question3(first_list: List[int], second_list: List[int])-> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


# O(N * 1) = O(N)
def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


# O(1 + N * N + 1) = O(N^2)
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


# O(log N)
def question6(n: int) -> int:
    i = 0
    while n > 1:
        i += 1
        print(f'n={n}')
        print(f'i={i}')
        n /= 2

    return n

