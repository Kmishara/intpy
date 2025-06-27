a = int(input("enter a number: "))

if a % 2 == 0:
    a -= 1

series = [2 * i+ 1 for i in range(a)]

print(",".join(map(str,series)))