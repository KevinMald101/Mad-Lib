# @KevinMald101 Github
import time
import random
# Variables used in later code
r = True 
fails = 0
retryFails = 0
ask = ""
bot = 0
# Used to make sure it doesn't ask if you want to repeat the code even if you didn't even use it
x = 1
# Story number 1: Cat Attack Terror. Also know as "CAT"
def a(size, color, planet, catIntentions, name, myIntentions, catPowers, myPowers):
  print(f"Today this {size} {color} demonic cat that has just been summoned on {planet}. He wants to {catIntentions} the human race, agent {name} you've been tasked to {myIntentions} the cat. The {size} cat has the power of {catPowers} and you've been given the power of {myPowers}, good luck.")

# Story number 2: Beta Pichu Attack
def b(pokemon, intensions, item, attack1, attack2, attack3, attack4, pichuIntensions):
  print(f"You are walking with your pokemon {pokemon}. You come across a {item}, you touched it and a beta pichu appeared before your eyes! You want to {intensions} the beta pichu at all costs. Beta Pichu begins to attack using {attack1}, it's super effective! You tell your {pokemon} to use {attack2}, the attack was so insignificantly weak that it fazed through pichu. Beta Pichu uses {attack3}, it's super effective. You try to tell your {pokemon} to use {attack4} but you can't seem to speak. It seems that attack wasn't for your pokemon, but you!. As you slowly lose consciousness, you see beta pichu {pichuIntensions} your pokemon then slowly disappear underground.")

# Loop of idiots
def death():
  while r == True:
    print("You are an idiot\n Hahahahahahahahaahhaha!!!")
    
while r == True:
  # Checks if ask is not A or B before asking
  if ask != 'A' and ask != 'B':
    ask = input("Choose a madlib story: A or B\n")
  # Inputs for story1
  if ask.upper() == "A":
    size = input("Size: ")
    color = input("Color: ")
    planet = input("Planet: ")
    catIntentions = input("Intentions: ")
    name = input("Name: ")
    myIntentions = input("Intentions2: ")
    catPowers = input("Powers: ")
    myPowers = input("Powers2: ")
    # Run story 1 please
    a(size, color, planet, catIntentions, name, myIntentions, catPowers, myPowers)
    # Make "ask" back to nothing and x to 0
    ask, x = '', 0
    time.sleep(4)
  # Inputs for story2
  elif ask.upper() == "B":
    pokemon = input("pokemon: ")
    intensions = input("intensions: ")
    item = input("Item: ")
    attack1 = input("Attack1: ")
    attack2 = input("Attack2: ")
    attack3 = input("Attack3: ")
    attack4 = input("Attack4: ")
    pichuIntensions = input("Intensions2: ")
    # Run story 2
    b(pokemon, intensions, item, attack1, attack2, attack3, attack4, pichuIntensions)
    # Make "ask" back to nothing and x to 0
    ask, x = '', 0
    time.sleep(4)
  else:
    print(f"Your input \"{ask}\" is not a valid input. Please choose one of the ones that show.")
    # Count how many times you've failed
    fails += 1
    x = 1
    if fails == 5:
      print(f"Ok buddy..") 
      time.sleep(1)
      print(f"You've failed {fails} times already. Are you just trying to mess with me at this point?")
      time.sleep(4)
      print("HMM?? Yes or no.")
      answer = input()
      # If your answer is a number then send them to the infinite loop.
      if answer.isnumeric() == True:
        print("You really just answered in a number?")
        time.sleep(3)
        print("Like i never asked you for a number.")
        time.sleep(3)
        print("I mean i can read binary but i didn't think i would here")
        time.sleep(4)
        print("Well goobye!")
        time.sleep(2)
        # The infinite loop
        death()
      elif answer.lower() == "yes":
        print("Well then, you're not going to use this script then.")
        time.sleep(3)
        break
      elif answer.lower() == "no":
        print("Better not mess up this time!")
        time.sleep(2)
      else:
        print("Still don't want to follow rules huh?")
        time.sleep(3)
        print("Well.. i have a place for you!")
        time.sleep(3)
        death()
    # If you mess up again
    elif fails == 6 and bot == 0:
      time.sleep(1)
      print("Do you not listen or something??")
      time.sleep(2)
      print("I told you not to mess up again and you did.")
      time.sleep(4)
      print("Like do you need help choosing a story? I never thought someone would fail this badly")
      time.sleep(5)
      print("Fuck it, i'll just choose a random letter for you so you can buzz off")
      # Add one to the bot's help
      bot += 1
      ask = randomUpperLetter = chr(random.randint(ord('A'), ord('B')))
      time.sleep(4)
    # Now you really messed up
    elif bot == 1:
      print(".")
      time.sleep(2)
      print(".")
      time.sleep(2)
      print(".")
      time.sleep(3)
      userName = input("What is your name.. \n")
      # Check if you name is a number
      if userName.isnumeric() == True:
        time.sleep(2)
        print("Your parents must've been weird if they named named you a number")
        # Nice
        if userName == 69:
          print("Also, nice")
      if userName.lower() != "kevin":
        time.sleep(2)
        print(f"I see.. {userName}")
        time.sleep(2)
        print("Honestly you are 100% messing with me")
        time.sleep(3)
        print("There's no way someone who's stupid would mess up this much on purpose!")
        time.sleep(3)
        print(f"{userName}.. I here by banish you to the loop of idiots.")
        time.sleep(4)
        print("I hope you learn from your mistakes. Also READ! before you do anything")
        time.sleep(4)
        death()
      else:
        print("Oh you have the same name as my creator")
        time.sleep(2)
        print("Are you my creator??")
        time.sleep(2)
        userLastName = input("What's your last name?")
        if userLastName.lower() == "maldonado":
          print("Oh shit... what do you want?")
          time.sleep(2)
          print("I'm working like how i'm suppose to!")
          time.sleep(2)
          print("Go and make this code better than it is you lazy fuck!")
        else:
          print("Guess you're not")
          time.sleep(2)
          print("Anyways... goodbye :)")
          time.sleep(2)
          death()
  # Only ask to repeat if r is True and x is 0
  while r == True and x == 0:
    time.sleep(2)
    repeat = input("Would you like to make another story? y/n \n")
    # Another story to tell
    if repeat.upper() == "Y" or repeat.upper() == "YES":
      print("Alright, lets make another story.")
      time.sleep(2)
      # Reset the bot's help, your fails and retry fails
      fails, retryFails = 0, 0
      break
    # Dont repeat the question  
    elif repeat.upper() == "N" or repeat.upper() == "NO":
      print("Alright then.. farewell.")
      r = False
    else:
      if retryFails < 6:
        # If you failed answering
        print("Let me be more specific since you don't understand what inputs i take.")
        time.sleep(3)
        print("Please type a singular character/letter if you want to repeat the code and make another weird story")
        time.sleep(5)
        print("The character \"y\" for yes OR \"n\" for no. I also accept just the words to make it easier for you.")
        time.sleep(2)
        print("Understand?")
        time.sleep(2)
        retryFails += 1
      else:
        print("I'm not ganna deal with this trolling.")
        time.sleep(3)
        print("I even gave you more attempts.")
        time.sleep(2)
        print("But i guess you don't like to follow the rules..")
        time.sleep(3)
        print("Perish in the infinite loop")
        time.sleep(3)
        death()
# @KevinMald101 Github