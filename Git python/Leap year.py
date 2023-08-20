leapyear = int(input("Enter a year."))

if leapyear % 4 == 0:
  if leapyear % 100 != 0:
    print("Leap year!")
  elif leapyear % 100 == 0:
    if leapyear % 400 == 0:
      print("Leap year!")
    else:
      print("Not a leap year.")
else:
  print("Not a leap year.")
  