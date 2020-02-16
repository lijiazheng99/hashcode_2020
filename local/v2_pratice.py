from common.data_utils import get_data
from tqdm import tqdm
import numpy as np
def get_max_sum_segement(slices_max,slices_type_list):
    max_so_far = 0
    max_ending_here = 0
    mantain_list=[]
    index_start=0
    for index, each in enumerate(slices_type_list):
        max_ending_here = max_ending_here + slices_type_list[index]
        if max_ending_here < 0:
            max_ending_here = 0

        # if max_so_far < max_ending_here:
        #     max_so_far=
            # mantain_list.append((index,max_ending_here))
            # max_so_far = 0
            # max_ending_here = 0
    return mantain_list


def get_max_list(slices_max, slices_type_list):
    best = current = 0
    current_index = start_index = end_index = 0
    for index, i in enumerate(slices_type_list):
        if current + i > 0:
            current += i
        else:
            current, current_index = 0, index + 1
        if current > best and current <= slices_max:
            start_index, end_index, best = current_index, index + 1, current
    return start_index, end_index, best

    # n,r,d=0,0,0
    # start_index=-1
    # max_allowed=-1
    # while n!=len(slices_type_list):
    #     n,r,d=n+1,np.max([r,d+slices_type_list[n],0]),np.max(d+slices_type_list[n],0)
    #     if r<=slices_max:
    #         start_index=n
    #         max_allowed=r
    # return start_index,max_allowed


def count_max(a_example):
    slices_type_list = a_example[1]
    slices_max = a_example[0][0]
    return get_max_sum_segement(slices_max, slices_type_list)


if __name__ == '__main__':
    inputs = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in", "b_small_test.in"]
    inputs_dict = get_data(inputs)
    # use a_Example as testing
    a_example = inputs_dict["b_small_test"]
    print(count_max(a_example))
