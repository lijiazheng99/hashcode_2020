import random


def main(set_item):
	[sum_goal, count_num] = input().split(" ")
	number_list = input().split(" ")
	number_list = list(map(int, number_list))
	sum_goal=int(sum_goal)
	answer = [sum_goal]

	for i in range(0,set_item):
		random.shuffle(number_list)
		start = 0
		end = 0
		list_end=[0 for j in range(0,len(number_list))]
		list_store = [sum_goal for j in range(0,len(number_list))]

		curr_count = 0
		for j in range(0,len(number_list)):
			if (curr_count+number_list[j]) <= sum_goal:
				curr_count+=number_list[j]
				end=j
			else:
				while curr_count+number_list[j] >sum_goal:
					list_end[start] = end
					list_store[start] = sum_goal-curr_count
					curr_count-=number_list[start]
					start+=1
				curr_count+=number_list[j]
				end = j
		start_pos=list_store.index(min(list_store))
		smalleat = list_store[start_pos]
		if smalleat < answer[0]:
			answer=[list_store[start_pos]]
			for i in range(start_pos,list_end[start_pos]+1):
				answer.append(number_list[i])
	print(len(answer[1:]))
	for i in answer[1:]:
		print(i,end=" ")
	print()
		

if __name__ == '__main__':
	set_item=100000
	main(set_item)