print("Numbers please, exit condition set to 11:");
nums = []
i = -5
total = 0
count = 0
while(i != 11):
    i = input()
    if(i.isdigit() != True):
        print("ERROR for string input")
    else:
        i = float(i)
        count = count + 1
        if(i != 11):
            nums.append(i)

if(count < 2):
    print("ERROR for less than 2 numbers")

for x in nums:
    total = total + x

if(total > 0):
    print("Here's your total:" , total)