data_dir = "../supplement/"

def get_data(inputs):
    inputs_dict = {}
    for each_in in inputs:
        with open(data_dir + each_in, "r") as f:
            data = []
            for each in f:
                data.append([int(i) for i in each.strip().split()])
            inputs_dict[each_in.split(".")[0]] = data
    return inputs_dict
