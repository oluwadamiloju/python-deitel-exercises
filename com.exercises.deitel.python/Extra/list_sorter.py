sample_list = [3, 2, 18, 0, 7, 6]
# smallest;


for number in sample_list:
    for i in sample_list:
        if number == 0:
            sample_list[0] = 0
        if number % 2 == 0 and number < sample_list[i]:
            sample_list[i] = number
            break
