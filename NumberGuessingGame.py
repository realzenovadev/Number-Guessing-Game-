import random 

#Get's user guess
def user(n):
  try:
    if n==1:
      guess=int(input("Enter Guessed Number: "))    
    else:
      guess=int(input(": "))
    return guess
  except ValueError:
    print("《 Please enter number only! 》 ")

#Get's random number 
def number():
  num=random.randint(1,100)
  return num


def check(user_guess,actual_number):
  if user_guess==actual_number:
    print(f"Correct it's {user_guess}")
  elif (actual_number-2)<user_guess and (actual_number+2)>user_guess:
    print("● Extremely close")
  elif (actual_number-5)<user_guess and (actual_number+5)>user_guess:
    print("● Very close")
  elif (actual_number-10)<user_guess and (actual_number+10)>user_guess:
    print("● Close!")
  elif (actual_number-20)<user_guess and (actual_number+20)>user_guess:
    if actual_number>user_guess:
      print("● Higher!")
    elif actual_number<user_guess:
      print("● Lower!")
  elif (actual_number-30)<user_guess and (actual_number+30)>user_guess:
    if actual_number>user_guess:
      print("● far higher!")
    elif actual_number<user_guess:
      print("● far Lower!")
  elif (actual_number-40)<user_guess and (actual_number+40)>user_guess:
    if actual_number>user_guess:
      print("● Much farther!")
    elif actual_number<user_guess:
      print("● Much lower!")
  else:
    if actual_number>user_guess:
      print("● Extremely higher!")
    elif actual_number<user_guess:
      print("● Extremely lower!")
  print("")

def play_or_quit():
  print("""Do you want to Play again or Quit?
  'P' for play again & 'Q' for quit""")
  choice=str(input(": ")).upper()
  while choice!="P" and choice!='Q':
    print("• Enter valid option (P/Q)!")
    choice=str(input(": ")).upper()
  return choice

def ask_mode():
  guess=0
  print("""Modes:       Number of Guesses:
  1■ Easy        (15)
  2■ Normal      (10)
  3■ Hard        (5)
  4■ Extreme     (3)
  5■ Impossible  (1)
  """)
  mode=str(input("Pick a mode(1-5): "))
  
  while True:
    try:
      mode=int(mode)
      if mode>=1 and mode<=5:
        break
      else:
        print("Please enter valid mode:")
        mode=str(input("Pick a mode(1-5): "))

    except ValueError:
      print("Please only enter number(1-5)")
      mode=str(input("Pick a mode(1-5): "))
  if mode==1:
    guess=15
  elif mode==2:
    guess=10
  elif mode==3:
    guess=5
  elif mode==4:
    guess=3
  elif mode==5:
    guess=1
    
  return guess

def check_game_status(point,guess_count, guess,streak):
  if guess_count>=guess:   
    print("Oops ran out of guesses")
    print(f"The number was {num}!")
    streak=0
    return point,streak
  else:
    point+=1
    streak=point
    return point,streak

def streak_msg(streak):
  if streak==0:
    print("Ahh ,Streak down to ZERO")
  elif 1 <= streak <= 3:
    print(f"Good start! Streak: {streak}")
  elif 4 <= streak <= 5:
    print(f"Nice, you're getting better! Streak: {streak}")
  elif 6 <= streak <= 8:
    print(f"Great job, strong streak! Streak: {streak}")
  elif streak == 10:
    print(f"Wow, 10 days streak! Streak: {streak}")
  elif 11 <= streak <= 15:
    print(f"Crazy consistency, respect! Streak: {streak}")
  elif streak > 15:
    print(f"Insane streak, don't break it! Streak: {streak}")
#main
print("Welcome to Number Guessing Game! ")
user_choice=str(input("Shall we play ? 'Y' for yes & 'N' for no : ")).upper()
while user_choice!='Y' and user_choice!='N':
  print('Invalid!')
  user_choice=str(input("Please enter valid choice (Y/N) : ")).upper()

point=0
streak=0
while user_choice=='Y':
  guess_count=1
  guess=ask_mode()
  print("Ok ,Guess the number 🧐")
  num=number()
  user_guess=0
  n=1
  while user_guess!=num and guess_count<=guess:
    guess_count+=1
    try:
      user_guess=user(n)
      user_guess=int(user_guess)
      while user_guess>100 or user_guess==0:
        print("Please enter number 1-100:")
        user_guess=user(n)
      check(user_guess,num)
      n=2
    except TypeError:
      print("Only numbers are allowed!")
  point,streak=check_game_status(point,guess_count,guess,streak)
  streak_msg(streak)
  print(f"Your points: {point}")
  choice=play_or_quit()
  if choice=='Q':
    user_choice='N'
    print("May you come back to play another time :D")

