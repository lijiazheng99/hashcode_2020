data_dir = "supplement/"
from tqdm import tqdm

import numpy as np
import itertools

def get_data(inputs):
    inputs_dict = {}
    for each_in in inputs:
        with open(data_dir + each_in, "r") as f:
            data = []
            for each in f:
                data.append([int(i) for i in each.strip().split()])
            inputs_dict[each_in.split(".")[0]] = data
    return inputs_dict

def get_max_list(slices_max,slices_type_list):
    max_list=[]
    min_value=1e12
    for e in range(0, len(slices_type_list) + 1):
        for subset in tqdm(itertools.combinations(slices_type_list, e)):
            left_value=slices_max-np.sum(subset)
            if subset != () and left_value>=0 and left_value<min_value:
                min_value=left_value
                max_list=subset
    return max_list

def count_max(a_example):
    slices_type_list=a_example[1]
    slices_max=a_example[0][0]
    return get_max_list(slices_max,slices_type_list)

if __name__ == '__main__':
    inputs = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
    inputs_dict=get_data(inputs)
    print(inputs_dict)
    # use a_Example as testing
    a_example=inputs_dict["a_example"]
    print(count_max(a_example))






