import math


def calculate_number_of_primes(first_number, last_number):

    # find square root of the largest number
    square_root_floor = math.floor(math.sqrt(last_number))
    number_of_primes = 0

    # find all the primes lower than the floor of the largest number's square root
    primes_to_test = find_primes_lower_than(square_root_floor)

    print(primes_to_test)

    # loop through each number and check for the primes lower than the number
    for i in range(first_number, last_number + 1):
        for j in range(2, len(primes_to_test) + 1):
            if i <= primes_to_test[j - 2]:
                print(i)
                number_of_primes += 1
                break
            
            if i % primes_to_test[j - 2] == 0:
                pass
            else:
                pass
                
            

    print("there are %d primes between %d and %d" %(number_of_primes, first_number, last_number))


def find_primes_lower_than(number) -> list:
    # find the square root of the number
    square_root_floor = math.floor(math.sqrt(number))

    primes = []

    # if the square root of the number is less than two, all the numbers in the set are primes.
    # otherwise, repeat the function with numbers lower than the floor of the square root

    if square_root_floor >= 2:
        primes2 = find_primes_lower_than(square_root_floor)

        # loop through all numbers and see if they are primes
        for i in range(1, number + 1):
            for j in range(1, len(primes2) + 1):
                if i < primes2[j - 1]:
                    break
                
                if i == primes2[j - 1]:
                    primes.append(i)

                if i % primes2[j - 1] != 0:
                    primes.append(i)
                    break
                else:
                    pass

        # ønsket utfall: [2, 3]
        return primes
    else:
        for i in range(1, number):
            primes.append(i + 1)

        return primes


calculate_number_of_primes(1, 10)
