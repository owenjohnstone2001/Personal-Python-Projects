global i
global x
global counter

i = [1]
x = 1
counter = 0

def fibb(length):
    global i, x, counter
    if length <= len(i):
        for item in i:
            print(item, '\n')
    else:
        i.append(x)
        x += i[counter]
        counter += 1
        fibb(length)

def prime(num):
    check = False
    for i in range(2,10):
        if num % i == 0:
            check = True
            break
        else:
            check = False
    if check == False:
        print(str(num) + " is prime.")
    else:
        print(str(num) + ' is not prime.')