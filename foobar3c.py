def solution(M_input, F_input):         #could implement tree but doing mass subtraction seems like easier solution for now
    M = int(M_input)
    F = int(F_input)
    iterations = 0
    if M == F: return "impossible"
    while True:
        if M == 1 and F == 1: return str(iterations)
        if M < 1 or F < 1: return "impossible"
        else: M, F, iterations = cycles(M, F, iterations)

def cycles(M, F, iterations):
    if M > F:                   #starting from bomb goal given and work our way down to 1.
        test = M / F
        if test > 2:
            M -= (F * (test - 1))       #some slight optimizations speeding up subtractions process
            iterations += test - 1      #how many times will we subtract in a row, if more than 2, do it all at once
        else:
            M -= F
            iterations += 1

    elif F > M:
        test = F / M
        if test > 2:
            F -= (M * (test - 1))
            iterations += test - 1
        else:
            F -= M
            iterations += 1
    else:
        return -1, -1, -1           #if equal, impossible
    return M, F, iterations
