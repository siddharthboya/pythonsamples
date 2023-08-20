import random

choice = int(input("Type 1 for rock, 2 for paper and 3 for scissors. Choose wisely!"))
cpu = random.randint(1,3)

if choice == 1 and cpu == 2:
  print("The computer chose paper and you chose rock. You lose.")
elif choice == 2 and cpu == 1:
  print("The computer chose rock and you chose paper. You win.")
elif choice == 1 and cpu == 3:
  print("The computer chose scissors and you chose rock. You win.")
elif choice == 3 and cpu == 1:
  print("The computer chose rock and you chose scissors. You lose.")
elif choice == 3 and cpu == 2: 
  print("The computer chose paper and you chose scissors. You win.")
elif choice == 2 and cpu == 3:
  print("The computer chose scissors and you chose paper. You lose.")
elif choice == 1 and cpu == 1:
  print("The computer chose rock and you chose rock. It's a draw.")
elif choice == 2 and cpu == 2:
  print("The computer chose paper and you chose paper. It's a draw.")
elif choice == 3 and cpu == 3:
  print("The computer chose scissors and you chose scissors. It's draw.")
else:
  print("Please re-run the program and type only 1, 2 or 3.")
  
