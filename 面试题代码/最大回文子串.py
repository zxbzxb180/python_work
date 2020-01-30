def word(lst):
    word_len = 1
    word_str = ''
    if len(lst) == 1:
        print(1, lst[0])
    else:
        for a in range(1, len(lst)):
            for i in range(len(lst)-a):
                lst_1 = lst[i:i+a]
                if lst_1 == lst_1[::-1]:
                    word_str = lst_1
                    word_len = a

        print(word_len, word_str)
lst = 'a'
word(lst)

#递归法
def isHuiWen(str):
    if(len(str) <2):
        return True
    if str[0] !=str[-1]:
        return False

    return isHuiWen(str[1:-1])