# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count >= 10:
        return 'Number of donuts: many'
    else:
        return 'Number of donuts:', count


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) > 2:
        return s[:2] + s[-2:]
    else:
        return ''


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    new_string = s[0] # make new string with first letter of given string
    for i in s[1:len(s)]: # traverse through s, starting with 2nd letter
        new_string += i.replace(s[0], '*') # and replace letters that match the first letter with '*'
    return new_string


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) >= 3:
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s + 'ing'
    else:
        return s


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    pos_n = s.find('not') # find 'not' in string and store index
    pos_b = s.find('bad') 
    if pos_b > pos_n:
        new_string = s.replace(s[pos_n:pos_b+len('bad')], 'good') # replace slice of string from start of 'not' to end of 'bad' with 'good'
        return new_string
    else:
        return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    # slice up a
    if len(a) % 2 == 0:
        afront = a[:len(a)/2]
        aback = a[len(a)/2:]
    else:
        afront = a[:len(a)/2+1]
        aback = a[len(a)/2+1:]
    
    # slice up b
    if len(b) % 2 == 0:
        bfront = b[:len(b)/2]
        bback = b[len(b)/2:]
    else:
        bfront = b[:len(b)/2+1]
        bback = b[len(b)/2+1:]
    
    # return compiled string
    return afront + bfront + aback + bback

    '''
    @ reshama: is there a better way to write this last one that doesn't require repeating the same if/else test on a and b?
    I tried writing another function within the function and calling it on each, but I couldn't run it on both a and b
    because 'return' would end the function.
    '''
