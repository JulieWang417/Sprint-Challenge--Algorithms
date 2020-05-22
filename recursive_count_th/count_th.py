'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
   
    # check if the word only contains 1 single letter
    if len(word) < 2:
        return 0
    # if the word more than 2 letters, checck the first two
    else :
        if str(word)[:2] == "th":
            return count_th(word[1:]) + 1 # we might need think about if the second place is letter "t"
        # for example, "other"
        # so we need start from index 1 for the next recursion
        else:
            return count_th(word[1:])



#print(count_th("otherthyuuuuth"))

# The time complexity is exponential O(n).
