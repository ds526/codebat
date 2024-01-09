def extra_end(str):
  str_len = len(str)
  if str_len < 3:
    return (str[0] + str[1]) * 3
  else:
    return (str[str_len - 2] + str[str_len - 1]) * 3
