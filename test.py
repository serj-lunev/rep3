with open('file.txt', 'r') as file:
  mass = float(file.readline())
  if mass > 3.0 and mass < 3.2:
    print(mass)
    print("mass is in [3, 3.2]")
  else:
    raise Exception('mass is not in [3, 3.2]')