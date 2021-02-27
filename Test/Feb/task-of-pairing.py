def taskOfPairing(freq):
    sol = 0
    carry = 0
    for i in freq:
        if i == 0:
            carry = 0
            continue
        if carry:
            sol += (i + carry) // 2
            carry = (i + carry) % 2
        else:
            sol += i // 2
            carry = i % 2
            
    return sol
