def cumsum_and_erase(A, erase = None):
    B = []
    for i in range(len(A)):
        summa = sum(A[:i+1])
        if summa != erase:
            B.append(summa)
    return B