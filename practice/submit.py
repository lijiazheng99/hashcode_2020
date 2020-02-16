from common.data_utils import get_data

inputs = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
inputs_dict = get_data(inputs)
sub_dir="../subs/practice/"
src_subs=["a.out","b.out","c.out","d.out","e.out"]

for index,each in enumerate(src_subs):
    sub_line2=[]
    lines = []
    with open(sub_dir+each) as f:
        for line in f:
            lines.append([int(i) for i in line.strip().split()])
        for e in lines[1]:
            index_here=inputs_dict[inputs[index].split(".")[0]][1].index(e)
            sub_line2.append(index_here)
            inputs_dict[inputs[index].split(".")[0]][1][index_here]=-1

    with open(sub_dir+"target_"+each,"w") as f2:
        f2.write(" ".join([str(e) for e in lines[0]])+"\n"+" ".join([str(e) for e in sub_line2])+"\n")




