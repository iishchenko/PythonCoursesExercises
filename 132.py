def down_counter(current_number):
    print(current_number)
    if current_number == 0:
        return 0
    else:
      down_counter(current_number - 1)

print(down_counter(5))
