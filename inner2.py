import third

def Inner():
  print('====inner2====')
  print(third.global_variable)
  third.Pop()
  print(third.global_variable)
