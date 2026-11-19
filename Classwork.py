def find_largest(a, b, c):
    return max(a, b, c)

print(find_largest(10, 20, 30))


def reverse_string(s):
    return s[::-1]
print(reverse_string("hello_World"))

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("aeiou"))

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(calculate_average([1, 2, 3, 4, 5]))

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))

def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 3, 4, 5, 5]))

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

print(calculate_grade(29))

def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))

def find_max_min(lst):
    return max(lst), min(lst)

print(find_max_min([89,3,24,15, 67, 100]))

def seperate_numbers(lst):
    even_numbers = []
    odd_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

print(seperate_numbers([1, 2, 3, 4, 5,6,7,8,9,10]))

def merge_lists(lst1, lst2):

    return lst1 + lst2

print(remove_duplicates(merge_lists([1, 2, 3,4,5], [4, 5, 6,3,7,8,9])))


Prices = {
    "laptop": 250000,
    "mouse": 15000,
    "keyboard": 25000
}

def calculate_total(prices):
    return sum(prices.values())

print(calculate_total(Prices))