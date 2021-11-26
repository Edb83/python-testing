def even_number_of_evens(numbers):
    
    if isinstance(numbers, list):
        even_nums = sum([1 for n in numbers if n % 2 == 0])

        return True if even_nums and even_nums % 2 == 0 else False
        
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    print(even_number_of_evens([2, 4]))
