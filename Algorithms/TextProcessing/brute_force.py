def find_brute(text, pattern):
    """
    Find the lowest index of text that matches pattern
    """

    text_length, pattern_length = len(text), len(pattern)

    for i in range(0, text_length-pattern_length):
        pattern_index = 0
        text_index = i
        while (pattern_index < pattern_length):
            # if all elements are same till end, return i, loop out of main for loop
            # if anamoly is detecred, loop out of while, icrement i
            if(text[text_index] == pattern[pattern_index]):
                text_index = text_index + 1
                pattern_index = pattern_index + 1
            else:
                break
        if(pattern_index == pattern_length):
            return i

    return -1

T = "abacaabaccabacabaabb"
P = "abacab"

ans = find_brute(T, P)
print (ans)
