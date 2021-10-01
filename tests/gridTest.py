headerWidth = 9
index = 0
print("base= " + str(headerWidth))

def fitToGrid(n, b):
    digits = ""
    if n == 0:
        digits = "0"
        digits = str(int(digits)+1)
        return digits
    while n:
        digits = str(n % b) + digits
        n //= b
    digits = str(int(digits)+1)
    return digits

i=0
while i < 20:
    print(str(index) + " ---> " + fitToGrid(index, headerWidth))
    index +=1
    i +=1
