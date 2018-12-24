# https://redd.it/a72sdj
num = input("Enter 11 digit UPC: ")
while(len(num) != 11):
    num = "0" + num
    if len(num) > 11:
        print("String too long")
        exit()
if not num.isdigit():
    print("Not a digit")
    exit()
new_sum = 0
for i in range(0, len(num), 2):
    new_sum += int(num[i])
new_sum *= 3
for i in range(1, len(num), 2):
    new_sum += int(num[i])
M = new_sum % 10
if M == 0:
    print("Your digit is 0")
else:
    print("Your digit is " + str(10 - M))