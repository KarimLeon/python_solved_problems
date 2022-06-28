def swap_case(s):
    swapped = []
    for letter in s: 
      if letter == letter.upper(): swapped.append(letter.lower())
      else: swapped.append(letter.upper())
      
    return ''.join(swapped)


# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
