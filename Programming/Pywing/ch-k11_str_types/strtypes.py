#string type , str is object so i can call a methods
frogstar = '' #single quote
frogx = "A "

#more couple strings
multi_string = '''
- Built in Python
- Mooren
- does nasa requit a fbi at youtube
'''

frogx.capitalize();

# nine space 
ss = '{1:>9} , {0:<09}'.format(8,9)
print('ss : {}'.format(ss))


# format inside string
#f string
x = 100
ovg = 1000
fortine = f'x (or) ovg  is : {x} , {ovg}'
print(fortine)
