def guess_num(n):
    l = 0
    r = n

    while l<=r:
        mid_n =(l+r)>>2
        if guess(mid_n)==0:
            return mid_n
        elif mid_n==-1:
            r = m-1
        else:
            l = m+1


print(guess_num(10))