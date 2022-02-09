def solution(n):
    num = int(n)
    counter = 0
    while num != 1:
        if num % 2 == 0: num = num / 2              #if even just divide
        else:
            if num != 3:                            #3 is edge case I found and this handles it
                if ((num + 1) / 2) % 2 == 0: num += 1
                elif ((num - 1) / 2) % 2 == 0: num -= 1
                else: num += 1                              #prioritizes addition, but if addition makes following division odd
            else: num -= 1                                  #then we try subtraction, if same result, then just add

        counter += 1
    return counter
