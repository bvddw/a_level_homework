# https://www.codewars.com/kata/58cda88814e65627c5000045/train/python

def expanded_form(num):
    i = 10
    result = []
    num = str(num)
    ind = num.index('.')
    j = 10
    for i in range(len(num)):
        if i < ind:
            if int(num[i]):
                result.append(str(int(num[i]) * (10 ** (ind - i - 1))))
        elif i == ind:
            continue
        else:
            if int(num[i]):
                result.append(num[i] + '/' + str(j))
            j *= 10
    return ' + '.join(result)
