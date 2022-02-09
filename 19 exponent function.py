
def rtp(number, power):
    result = 1
    for el in range(power):
        result = result * number
    return result

a = int(input("Number: "))
b = int(input("Rise to Power: "))
print(rtp(a, b))