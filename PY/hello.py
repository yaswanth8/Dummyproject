def odd_or_even(number):
    """ Test odd or even """
    if number%2==0:
        return 'Even'
    else:
        return 'Odd'

odd_or_even_string=odd_or_even(6)
print(odd_or_even_string)
