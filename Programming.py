# Variables n = 0
n = 0
print('n =', n)

n = "abc"
print('n =', n)

# Mutliple assignmnets

n, m = 0, "abc"
n, m, z = 0.125, "abc", False


# Increment
n = n + 1
n += 1
# n++ not allowed

# None is null
n = 4
n = None
print("n =", n)

# If statements dont need parantheses | curly braces
n = 1 
if n>2:
    n-=1
elif n == 2:
    n*=2

# Parenteses needed for mutli-line conditions 
# and = &&
# or = ||

n, m = 1, 2
if ((n > 2 
     and 
     n!= m) or n ==m):
    n += 1

# While loops are similar 
n = 0 
while n < 5:
    print(n)
    n += 1

# looping from i = 0 to i = 4
for i in range(5):
    print(i)

# looping from i = 2 to i = 5
for i in range(2,6):
    print(i)

for i in range(5, 1, -2):
    print(i)

# Division is decimal by defalt 
print (5 / 2) # gives 2.5

# Doulbe slash rounds down
print(5 // 2)

# default so ngeative numbers will round down
print(-3 // 2)

print(int(-3/2))

# Max / Min Int
float("inf")
float("-inf")

import math 
print(math.pow(2, 200))