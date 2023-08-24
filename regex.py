import re

pattern=re.compile("(^[A-Z][a-z]+), ([A-Z][a-z]+)?[-]?([A-Z][a-z]+)?")
pattern2=re.compile("(\B@[a-z]+)+")
print('''
      ============================
          Full Name / Twitter
      ============================
      ''')
with open("names.txt") as f:
    data = f.readlines()
    x=0
    for c in data:
        name = pattern.findall(c)
        handle = pattern2.findall(c)
        if name and handle:
            if name[0][2] != '':
                fname = name[0][2]
                lname1 = name[0][1]
                lname2 = name[0][0]
                fullname = f'{fname} {lname1}-{lname2}'
            else:
                lname = name[0][0]
                fname = name[0][1]
                fullname = f'{fname} {lname}'

            handle = handle[0]
            fhandle = f'{handle}'
            
        
            print(f'{fullname} / {handle}\n')
        x+=1


# (env311) G:\Code Temple\week_4\day1>python -u "g:\Code Temple\week_4\day1\regex.py"

#       ============================
#           Full Name / Twitter
#       ============================

# Derek Hawkins / @derekhawkins

# Erik Sven-Osterberg / @sverik

# Ryan Butz / @ryanbutz

# Example Exampleson / @example

# Ripal Pael / @ripalp

# Darth Vader / @darthvader


# (env311) G:\Code Temple\week_4\day1>