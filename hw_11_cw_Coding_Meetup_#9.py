# https://www.codewars.com/kata/coding-meetup-number-9-higher-order-functions-series-is-the-meetup-age-diverse

def is_age_diverse(lst):
    yearsold = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in lst:
        n = i['age'] // 10
        if n < 10:
            yearsold[n - 1] += 1
        else:
            yearsold[9] += 1
    return False if 0 in yearsold else True