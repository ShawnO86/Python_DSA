
def get_sorted_run_length(integer_list, start_index):
    comp = start_index
    run_len = 0
    for i in range(start_index, len(integer_list) - 1):
        if integer_list[comp] <= integer_list[i]:
            run_len += 1
            comp += 1
    return run_len

nums = [15, 23, 23, 23, 31, 64, 77, 87, 88, 91]

print(get_sorted_run_length(nums, 10))