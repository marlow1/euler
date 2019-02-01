
'''
Problem 2350

Question:

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

Find find number chickens c and number of rabbits r such that c + r = 35 and 4r + 2c = 94

'''

def chines_petting_zoo(total_animals, number_legs):
    for c in range(1, total_animals + 1):
        if (2*c) + 4 * ((total_animals - c + 1)) == number_legs:
            return c, total_animals - c + 1


'''
problem 545

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


'''



if __name__=='__main__':
    print(chines_petting_zoo(35, 94))