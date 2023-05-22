# https://www.codewars.com/kata/coding-meetup-number-13-higher-order-functions-series-is-the-meetup-language-diverse

def is_language_diverse(lst):
    language = {'Python': 0, 'Ruby': 0, 'JavaScript': 0}
    for i in lst:
        language[i['language']] += 1
    return False if language['JavaScript'] > 2 * language['Python'] or language['JavaScript'] > 2 * language['Ruby'] or language['Python'] > 2 * language['Ruby'] or language['Python'] > 2 * language['JavaScript'] or language['Ruby'] > 2 * language['JavaScript'] or language['Ruby'] > 2 * language['Python'] else True