# https://www.codewars.com/kata/582887f7d04efdaae3000090

def find_senior(lst):
    max = 0
    for i in lst:
        if i['age'] > max:
            max = i['age']
    print(max)
    return [i for i in lst if i['age'] == max]