"""Q17) Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list. Use list comprehension to solve this problem.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Output: [2, 4, 6, 8, 10]"""

def get_even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]

input_str = input()#Enter the array elements separated by spaces:
input_list = list(map(int, input_str.split()))
output_list = get_even_numbers(input_list)
print(output_list)
