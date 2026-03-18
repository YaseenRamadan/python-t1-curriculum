import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_systems = ["Windows", "macOS", "Linux"]
print(operating_systems [len(operating_systems) - 1])
operating_systems.reverse()
print(operating_systems)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
SCHOOL_SUBJECTS = ["Math", "Science", "English", "History"]
print(SCHOOL_SUBJECTS[1])
SCHOOL_SUBJECTS.sort()
print(SCHOOL_SUBJECTS)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
error_codes = ["404", "500", "403", "401", "502"]
print(len(error_codes))
print(error_codes.index("403"))
# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
programming_languages = ["Python", "JavaScript"]
print(random.choice(programming_languages))
appended_language = "Java"
programming_languages.append(appended_language)
print(programming_languages)
# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords =["yaseen67", "876431", "mom/dad," , "t1y2u3i4", "password123", "secret456"]
print(passwords [len(passwords) // 2])
removed_passwords = passwords.pop(0)
print(passwords)