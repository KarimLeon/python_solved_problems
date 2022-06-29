def solve(s):
   names = s.split(' ')
   fullname = ''
   for i in range(len(names)):
      if names[i] == '': names[i] = '#'
      fullname += names[i][0].upper() + names[i][1:]
     
   return ' '.join(fullname.split('#'))

#STILL NEEDS TO BE SOLVED...
