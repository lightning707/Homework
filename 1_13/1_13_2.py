class MFilter:
    def remove_positives(self, lst):
        # result_lst = []
        # for num in lst:
        #     if num <= 0:
        #         result_lst.append(num)
        # return result_lst
        return [num for num in lst if num <= 0]

    def filter_leaps(self, lst):
        # result_lst = []
        # for year in lst:
        #     if year % 4 == 0:
        #         result_lst.append(year)
        # return result_lst
        return [year for year in lst if year % 4 == 0]


class MMath:
    def square_nums(self, lst):
        # result_lst = []
        # for num in lst:
        #     result_lst.append(num ** 2)
        # return result_lst
        return [num ** 2 for num in lst]


class Mathematician(MFilter, MMath):
    pass


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([-1, -5, 2, 7, 10]) == [-1, -5]
assert m.filter_leaps([1999, 2004, 2007, 2020]) == [2004, 2020]

