headerWidth = 9
index = 0
print("base= " + str(headerWidth))

def fitToGrid(n, b):
    digits = ""
    if n == 0:
        return 0
    while n:
        digits = str(n % b) + digits
        n //= b
    return digits

i=0
while i < 20:
    index +=1
    print(str(index) + " ---> " + fitToGrid(index, headerWidth))
    i +=1
