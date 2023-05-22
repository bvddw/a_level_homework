# https://www.codewars.com/kata/5842df8ccbd22792a4000245

def expanded_form(num):
    i = 10
    result = []
    num = str(num)
    num = num[::-1]
    for i in range(len(num)):
        if int(num[i]):
            result.append(str(int(num[i]) * (10 ** i)))
    return ' + '.join(result[::-1])
