def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number == 0 or number == 1:
        return number

    start = 0
    end = number
    res = 0
    i = 0
    while not res:
        i += 1
        if start == end:
            res = start
            break
        median = round(end - (end-start)/2)
        number_sqrt = median*median

        if number_sqrt == number:
            res = median
            break
        number_sqrt_next = (median+1)*(median+1)
        if number_sqrt > number:
            end = median
        else:
            if number_sqrt_next > number:
                res = median
                break
            start = median

    return round(res)

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (75 == sqrt(5625)) else "Fail")
print("Pass" if (123 == sqrt(15129)) else "Fail")
print("Pass" if (1234 == sqrt(1522756)) else "Fail")
print("Pass" if (274003 == sqrt(75078060840)) else "Fail")
print("Pass" if (18 == sqrt(345)) else "Fail")
