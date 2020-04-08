def func(val):
    return (((val - 1) ** 3) + (val ** 2))

def deriv(val):
    return ((3 * ((val - 1) ** 2)) + (2 * val))

x_1 = 5
real_root = 0.4302
count = 0

while abs(((x_1 - real_root)) / real_root) * 100 >= 0.01:
    x_1 = x_1 - (func(x_1) / deriv(x_1))
    count += 1

print(count)

