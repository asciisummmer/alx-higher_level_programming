#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    result_division = []
    for i in range(list_length):
        try:
            res = my_list1[i]/my_list2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            result_division.append(res)
    return result_division
