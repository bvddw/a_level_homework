# https://www.codewars.com/kata/coding-meetup-number-8-higher-order-functions-series-will-all-continents-be-represented

def all_continents(lst):
    areas = []
    count = 0
    for i in lst:
        if i['continent'] not in areas:
            areas.append(i['continent'])
    return True if len(areas) == 5 else False