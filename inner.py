import third

def Inner():
  print('====inner====')
  print(third.global_variable)
  third.Push(1)
  print(third.global_variable)
  


