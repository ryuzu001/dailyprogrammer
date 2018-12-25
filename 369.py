# https://redd.it/a0lhxx
def hexcolor(colors):
    col = colors.split(", ")
    if not len(col) == 3:
        print("Input error")
        exit()
    if not col[0].isdigit() or not col[1].isdigit() or not col[2].isdigit():
        print("Number error")
        exit()
    a = int(col[0])
    b = int(col[1])
    c = int(col[2])
    if a > 255 or b > 255 or c > 255:
        print("Range error")
        exit()
    return "#" + RGBtoHEX(a) + RGBtoHEX(b) + RGBtoHEX(c)
    
def RGBtoHEX(num):
    if num == 0 or num == 1:
        num *= 255
    a = int(num/16)
    if a < 10:
        ret = str(a)
    elif a == 10:
        ret = "A"
    elif a == 11:
        ret = "B"
    elif a == 12:
        ret = "C"
    elif a == 13:
        ret = "D"
    elif a == 14:
        ret = "E"
    else:
        ret = "F"
    a = num%16
    if a < 10:
        ret += str(a)
    elif a == 10:
        ret += "A"
    elif a == 11:
        ret += "B"
    elif a == 12:
        ret += "C"
    elif a == 13:
        ret += "D"
    elif a == 14:
        ret += "E"
    else:
        ret += "F"
    return ret

colors = input("Enter 3 numbers, seperated by comma and space: ")
print(hexcolor(colors))