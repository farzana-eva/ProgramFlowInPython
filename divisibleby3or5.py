for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue

    print(i)
print("---------------")

for x in range(21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)