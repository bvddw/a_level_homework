# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    times = {'second': seconds % 60, 'minute': seconds // 60 % 60, 'hour': seconds // 3600 % 24,
             'day': seconds // 86400 % 365, 'year': seconds // 31536000}
    result = []
    if seconds == 0:
        return 'now'
    for key, value in times.items():
        if value == 0:
            continue
        current = str(value) + ' ' + key
        current += 's' if value > 1 else ''
        result.append(current)
    result = result[::-1]
    return ', '.join(result) if len(result) == 1 else ', '.join(result[: -1]) + ' and ' + result[-1]