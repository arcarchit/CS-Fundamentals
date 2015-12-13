def last(last, pattern):
    """ indexing starts from 0 """
    all_char = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(all_char)):
        key = all_char[i]
        last[key] = -1
    for i in range(0, len(pattern)):
        key = pattern[i]
        last[key] = i


def boyer_moore(text, pattern):
    # First creating a dic to store position where characters occur at last
    last_dic={}
    last(last_dic, pattern)

    text_length, pattern_length = len(text), len(pattern)
    i = 0
    while (i <= text_length - pattern_length):
        text_index = i + pattern_length - 1#comparison starts from right
        pattern_index = pattern_length - 1
        while (pattern_index >= 0):
            if(text[text_index] == pattern[pattern_index]):#decrment if character matches
                text_index = text_index - 1
                pattern_index = pattern_index - 1
            else:
                bad_char = text[text_index]
                last_occurance_index_of_bad_char = last_dic[bad_char] #it will return an index

                #shift the pattern to align with bad character if it exists in pattern
                #else shift by entire pattern
                if(last_occurance_index_of_bad_char == -1):
                    i = i + pattern_length
                elif(pattern_index < last_occurance_index_of_bad_char):
                    i = i + pattern_length
                else:
                    i = i + pattern_index - last_occurance_index_of_bad_char
                break
        if(pattern_index == -1):
            return i
    return -1

T = "abacazsedsaabaccabacabaabb"
P = "abacab"

ans = boyer_moore(T, P)
print (ans)
