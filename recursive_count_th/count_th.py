'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if not word:
        return 0
    else:
        count = 1 if word[:2] == 'th' else 0
        return count + count_th(word[1:])


print(count_th('theethee'))
