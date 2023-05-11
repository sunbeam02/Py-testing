
def avg(**args):
    total = 0
    for num in args:
        if isinstance(num, int or float):
            total += num
        else:
            raise TypeError('Not an Integer 0r float')
    return int(total / len(args) )