
def is_palindrome(s):
    s = s.lower()
    cleaned_string = ''.join(c for c in s if c.isalnum())
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("Hello"))



# def find_max(list):
#     max_number = list[0]
#     for i in list:
#         if i > max_number:
#             max_number = i
#     return max_number
#
#
# def find_min(list):
#     min_number = list[0]
#     for i in list:
#         if i < min_number:
#             min_number = i
#     return min_number
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(find_max(numbers))
# print(find_min(numbers))

# def factorial(number):
#     if number == 0:
#         return 1
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     return result
#
# print(factorial(7))

# import math
# def is_prime(number):
#     if number < 1:
#         return False
#     for i in range(2, int(math.sqrt(number) + 1)):
#         if number % i == 0:
#             return False
#     return True
#
# print (is_prime(6))