estimate = 0
inp = ''

while inp.lower() != 'no':
    inp = input("Choose the end value for the summation: ")
    for n in range(1,int(inp)+1):
        estimate += (1 / (n ** 2))
    print(estimate, '\n')
    estimate = 0

