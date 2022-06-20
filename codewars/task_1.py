def square_sum(numbers):
    counter = 0
    sum = 0
    while len(numbers) > counter:
        sum += numbers[counter]**2
        counter += 1
    return sum


numbers_to_square = [0, 7, 9, 5, 77]

print(square_sum([1, 2, 2]))
print(square_sum(numbers_to_square))
print(square_sum([]))
