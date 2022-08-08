def bite(a,b):
    kol = 0
    a2 = (bin(a)[2:])
    b2 = (bin(b)[2:])
    if len(b2) > len(a2):
        a2 = a2 + ('0'*(len(b2) - len(a2)))
    elif len(b2) < len(a2):
        b2 = b2 + ('0' * (len(b2) - len(a2)))
    for i in range(len(a2)):
        if a2[i] != b2[i]:
            kol += 1
    return kol

print(bite(2429550120, 2429201960))

