def first_half(str):
  end_loop = len(str) / 2
  new_str = ""
  for i in range(0,end_loop):
    new_str+=str[i]
  return new_str
