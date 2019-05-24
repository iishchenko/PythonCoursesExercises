def wake_up(time, is_weekend):
  if is_weekend and time > 9:
    return True
  elif not is_weekend and time > 6:
    return True
  else:
    return False

wake_up(5)
wake_up(8, is_weekend = True)
