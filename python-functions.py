# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
# sum_to(6)  # returns 21
# sum_to(10) # returns 55


def sum_to(n):
  sum = 0
  for x in range(n+1):
    sum += x
  return sum

print(sum_to(6))

#Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(arr):
  l = 0
  for x in arr:
    if x > l:
      l=x
  return l

print(largest([10, 4, 2, 231, 91, 54]))

#Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

string = input('Enter string: ')
string2 = input('Enter second string: ')

#does not work 
# def occurances(str1,str2):
#   count = 0
#   for x in range(len(str1)):
#     if str1[x] == str2:
#       count += 1
#   return count

def occurances(string, substr):
  return string.count(substr)

print(occurances(string, string2))

# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.
# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0

def product(*args):
    product = 1
    for a in args:
        product *= a
    return product

print(product(4, 0.5, 5))



