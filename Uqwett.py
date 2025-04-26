numbers = [1, 0, 3.14, -2]


def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def change_direction(x):
    return x * -1

apply_to_each(numbers, change_direction)

print(numbers)



# def square(x):
#     return x * x

# apply_to_each(numbers, square)

# print(numbers) 



    

