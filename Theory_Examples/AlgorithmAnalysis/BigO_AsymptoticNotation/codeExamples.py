# Code Examples of Big-O

# 0. A constant algorithm - O(1)
data = 'Hello';       
x = 3;                

if data == 'Hello':   
    print(data * x) 

# 1. A logarithmic algorithm - O(logn)
num = 16
count = 0
while num > 1:
    num /= 2
    count += 1

# 2. A linear algorithm – O(n)
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num

# 3. A superlinear algorithm – O(nlog[n])
n = 5
for i in range(n):
    for j in range(i):
        print(i, j)

# 4. A polynomial algorithm – O(n^c)
n = 5
for i in range(n):
    for j in range(n):
        print(i, j)

# 5. A exponential algorithm – O(c^n)
n = 5
for i in range(2 ** n):
    print(i)

# 6. A quadratic algorithm – O(n^2)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, j)

# 7. A cubic algorithm – O(n^3)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            print(i, j, k)

