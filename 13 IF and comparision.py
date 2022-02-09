x = input("input 3 numbers\n number 1:")
y = input("number 2: ")
z = input(" and : ")

def p_hn():


    hnz = [x, y, z]
    hnz.sort()
    hn = (hnz[-1])
    return hn

def ln(x, y, z):
    if x <= z and x <= y:
        return x
    elif z <= x and x <= y:
        return z
    else:
        return y

print("highest number is " + p_hn() + " and lowest is " + ln(x, y, z) )


