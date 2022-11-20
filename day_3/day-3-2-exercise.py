height = int(input("How tall are you? "))
age = int(input("How old are you? "))
if height > 120:
  print("Can ride")
  
  if age > 18:
    print("$12")
  elif age >= 12:
    print("$7")
  else:
    print("$5")
  
else:
  print("Can`t ride")