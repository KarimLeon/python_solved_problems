def swap_case(s):
    swapped = []
    for letter in s: 
      if letter == letter.upper(): swapped.append(letter.lower())
      else: swapped.append(letter.upper())
      
    return ''.join(swapped)


