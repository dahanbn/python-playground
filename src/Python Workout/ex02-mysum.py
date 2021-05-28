def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(1, 2, 3, 4))
print(mysum(*[1, 2 ,3 ,4]))
