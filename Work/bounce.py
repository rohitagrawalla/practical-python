# bounce.py
#
# Exercise 1.5

height = 100

for i in range(1, 11):
    height *= 3.0 / 5.0
    print(f"{i} {round(height, 4)}")
