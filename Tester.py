m = int(input(""))
n = int(input(""))

if m == n:
    print(m)
    
elif m < n:
    n = n + 1
    for i in range(m, n):
        if (i + 1) % 10 == 0 or i % 17 == 0 or i % 15 == 0:
            print(i)


n = int(input(""))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)