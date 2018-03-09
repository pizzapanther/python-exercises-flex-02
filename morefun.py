def hello (name):
  print('Hello {}'.format(name))
  
def hello2 (name):
  return 'Hello {}'.format(name)
  
def hello3 (*args, **kwargs):
  print(args)
  print(kwargs)
  
print(hello('Paul'))
print(hello2('Paul'))
print(hello3('Paul', 'B', 'M', food="pizza"))