# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    meet_time = {}
    for i in seq:
        if i not in meet_time.keys():
            meet_time[i] = 1
        else:
            meet_time[i] += 1
    for key, value in meet_time.items():
        if value % 2:
            return key