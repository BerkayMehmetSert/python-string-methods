website = 'http://www.google.com'
course = 'Python Programming Language for Beginners'

# 1. Deleting the first character and last characters of the 'Hello World' string
result = 'Hello World'.strip() # strip() method removes the first and last characters of the string
print(result)

# 2. How many 'o' characters are in the 'website' string
result = website.count('o') # count() method counts the number of 'o' characters in the string
print(result)

# 3. Replace the 'Python' string with 'Java' in the 'course' string
result = course.replace('Python', 'Java') # replace() method replaces the first occurrence of the string with the second string
print(result)