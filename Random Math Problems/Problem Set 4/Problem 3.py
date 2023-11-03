# What is the smallest integer that can result when a five-digit positive integer is divided by the sum of its digits?

smallest = 1000000000000000

for i in range(10000, 100000):
    (i // 10000 + i // 1000 % 10 + i // 100 % 10 + i // 10 % 10 + i % 10)
    if i %  == 0:
        if 