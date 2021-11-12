import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list=[rock, paper, scissors]

H=int(input("enter 0 for rock, 1 for paper, 2 for scissors: "))
C=int(random.randint(0,2))
print(C)
print(f"{list[H]}\n")
print(f"{list[C]}\n")

if H>=3 and H<0:
  print("Invalid")
elif H==0 and C==2:
  print("you Win")
elif C==0 and H==2:
  print("you lose")
elif C>H:
  print("You lose")
elif H>C:
  print("you win")
elif H==C:
  print("draw")
