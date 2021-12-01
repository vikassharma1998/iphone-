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

import random
list=[rock,paper,scissors]

user=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(user)
computer=random.randint(0,2)
print(computer)
print(list[user])
print(list[computer])

if user==0 and computer==2:
    print("you win")
    
elif user==2 and computer==1:
    print("you win")
    
elif user==1 and computer==0:
    print("you win")
elif user==computer:
    print("Match Drow")
elif user<=3 or user<0:
    print("wrong number you enter ")    
    
else:
    print("you lose")
    
