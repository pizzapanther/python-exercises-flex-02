raw_input = input('age? ')
age = int(raw_input)

if age >= 21:
    print('You get beer')
elif age < 18 or age > 10:
    print('get lost')
else:
    print('Sorry')
    