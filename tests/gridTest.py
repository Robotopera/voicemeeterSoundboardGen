headerWidth = 8
index = 0

def numberToBase(n, b):
    digits = ""
    if n == 0:
        return 0
    else:
        digits = str(n % b) + digits
    return digits

i=0
while i < 20:
    index +=1
    print(str(index) + " ---> " + numberToBase(index, 8))
    i +=1
