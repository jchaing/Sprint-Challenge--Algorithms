'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # base case
    # check if none or only 1 letter is in word
    if len(word) == 0 or len(word) == 1:
        return 0

    # if first letter is 't' and second letter is 'h'
    elif word[0] == "t" and word[1] == "h":

        # recurse from second letter and add 1
        return count_th(word[1:]) + 1

    # otherwise
    else:

        # recurse starting from the second letter
        return count_th(word[1:])


print(count_th("fourth"))  # 1
print(count_th("thththth"))  # 4
print(count_th("fourthfourt"))  # 1
print(count_th("thfourth"))  # 2
print(count_th("sithfifith"))  # 2
