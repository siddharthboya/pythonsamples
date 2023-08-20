days = 365 * 90
weeks = 52 * 90
months = 12 * 90

age = int(input("What is your age:"))

days -= (365 * age)
weeks -= (52 * age)
months -= (12 * age)
print(f"So let's say you live to ninety, or you have {days} days, {weeks} weeks, or {months} months.")    
