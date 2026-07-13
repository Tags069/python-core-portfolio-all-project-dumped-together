#PROJECT 1 (malbids game) EASY

# name=input('What is your name?: ')
# age=input('What is your age?:')
# int(age)
# country=input('What is your country?: ')
# city=input('What is your city?: ')
# phone_number=input('What is your phone number?: ')
# int(phone_number)

# print(f'hello my name is {name} and i am this years {age} and i am from the country of {country} and city of {city} my phone number is {phone_number}')


#PROJECT 2(calculator project) EASY

# num_1 = float(input('Choose a first number: '))
# num_2 = float(input('Choose a second number: '))

# operaters = input('Choose an operator (+, -, /, *): ')

# if operaters == '+':
#     result = num_1 + num_2
#     print(f"The answer is: {result}")
    
# elif operaters == '-':
#     result = num_1 - num_2
#     print(f"The answer is: {result}")
    
# elif operaters == '/':
#     result = num_1 / num_2
#     print(f"The answer is: {result}")
    
# elif operaters == '*':
#     result = num_1 * num_2
#     print(f"The answer is: {result}")
    
# else:
#     print('Invalid operator! Please run the program again.')

#PROJECT 3(temprature convertion) EASY

# temp_value=float(input('Chosse temprature value:'))
# Convertion=input('Pick betweeen Celcuis(C) or Fahrenheit(F) to convert and vise versa:')

# if Convertion.upper()=='C':
#     coverted_value=temp_value*9/5 + 32 
#     print(f'Your new temprature from celcuis to fehrenheit is {coverted_value}')

# elif Convertion.upper()=='F':
#     coverted_value=(temp_value - 32) * 5/9
#     print(f'Your new temprature from  fehrenheit  to celcuis is {coverted_value}')

# else:
#     print('unknown  value/invlaid response in the terminal')


#PROJECT 4 (driver licinces) EASY

# age=int(input('what is ur age:'))

# classes=input('have you taken classes yes or no?:')

# if age>=18 and classes.upper()=='YES':
#     print('Your are elgiblabe')

# elif age<18 and classes.upper()=='YES':
#     print('sorry u are to young to drive')   
    
# elif age>=18 and classes.upper()=='NO':
#     print('sorry u  dont have the classes ')    

# elif age<=18 and classes.upper()=='NO':
#     print('sorry you have to be older and take classes') 

# else:
#     print('invlaid stamtent')    


#PROJECT(5) ESCAPE ROOM EASY-MID

# print("--- WELCOME TO THE ESCAPE ROOM ---")
# print("You are locked in a room. To escape, you must find a KEY and a CODE.")
# print("Type 'search', 'door', or 'quit' to play.\n")

# attempt = 0
# key = False
# paper = False

# while True:
#     computer = input('What do u want?: ').upper().strip()

#     if computer.upper() == 'QUIT':
#         print('Sorry u have failed try again')
#         break 

#     elif computer.upper() == 'DOOR':
#         if key  and paper:
#             print('CONGRATS you HAVE ESCAPED! ')
#             break 
#         else:
#             print('The door is locked tight. You are missing something. Try searching!')

#     elif computer.upper() == 'SEARCH':
#         attempt += 1
        
#         if attempt == 3:
#             key = True
#             print('Congrats u have found the key')
#         elif attempt == 5:
#             paper = True
#             print('Congrats u have found the paper code')
#         else:
#             print('U kept searching but you have found nothing.')
            
#         if paper and key:
#             print('You have everything! Try to open the door!')

#     else:
#         print('invalid option')

#PROJECT (6) STOP WACTH TIMER EASY

# import time

# print('ROCKET LAUNCH')

# countdown=int(input('chosse the number to count down from in secs:'))

# for i in range(countdown,0,-1):
#     time.sleep(1)
#     print(i)

# print('ROCKET LAUNCH ')    


#Messy paragraph 

# paragraph=[]
# user_paragraph=input('enter your word ot make a pargragha').split()
# paragraph+=user_paragraph
# paragraph=paragraph.pop(0).capitalize()+str(f'{paragraph,paragraph.pop(-1).lower()}')
# clean_pargrapha=''.join(paragraph)
# print(clean_pargrapha)


#Rolleer coster program

# print('WELCOME TO ROLLER COSTER')

# heghit_check=int(input(('what is your heghit?:')))

# if heghit_check>=120:
#     age_check=int(input(('what is your age:?')))
#     if age_check>=10:
#         print('you are allowed welocome to the ride ')

#     else:
#         print('sorry u have to ask a gardian or parents permisssion:')
#         Permission=input(('do u give your child persmisson Yes or no ')).upper()
#         if  Permission=='YES':
            
#             print('Welcome your allowed on the roller coster')
#         else:
            
#             ('sorry your parents have dined permission')

# else:
#     print('sorry ur to short to get on the the ride')           
        

#Grade boundries assesment

# Grade_input=int(input('What are your grades?:'))

# if Grade_input<0:
#     print('unknown value')


# elif Grade_input>=90:
#     print('Final grade:A')

# elif Grade_input>=80<=89:
#     print('FInal Grade:B')

# elif Grade_input>=70<=79:
#     print('FInal Grade:C')

# elif Grade_input>=60<=69:
#     print('FInal Grade:D')

# elif Grade_input<60:
#      print('Final grade:F')


# else:
#     print('invalid input')




#Dark room escape 

# print('Welcome to the dark rooms')

# person_choice=input('hello welcome please chosse the door to Your right/Left:').upper()

# if person_choice == 'LEFT':
#     print('sorry there is nothing to be found try going back to the right room ')
#     person_choice=input('Would u like to go to another room yes or no')
#     if person_choice =='Yes':
#         print('You found a chest and a locked door')
#     if person_choice == 'YES':



# elif
# person_choice == 'RIGHT':
#     print('You found a chest and a locked door')
#     person_choice = input('would u like to open a chest yes or no:?').upper()
    
#     if person_choice == 'YES':
#         print('You have found a key')
#         person_choice = input('would u like to try to use the key on the door  yes or no :?').upper()
        
#         if person_choice == 'YES':
#             print('congrants u have have escaped ')
#         else:
#             print('you kept standing there:')
            
#     else:
#         print('you chose not to open the chest')

# else:
#     print('sorry u have failed u kept standing there')

# if person_choice=='RIGHT':
#     print('You found a chest and a locked door')
#     person_choice=input('would u like to open a chest yes or no:?')
# elif person_choice=='YES':
#     print('You have found a key')
# else:
#     print('sorry u have failed u kept standing there')
# person_choice=input('would u like to try to use the key on the door  yes or no :?') 

# if person_choice=='YES':
#     print('congrants u have have escaped ')
# else:
#     print('you kept standing there:')


#Security system clerance

# bagde=input('do u have an bage on u right now?').upper()

# if bagde=='YES':
#     bagde=True
# else:
#     bagde=False

# postistion=input('what is your current postion:').upper

# if postistion=='STAFF' or postistion=='MANGER':
#     postistion=True
# else:
#     postistion=False


# if bagde==True and postistion==True:
#     print('accses granteed welcome')
# else:
#     print('acces DINIED')    


#Temprature CONTROLLING
# temp=int(input('What is the temp right now?:'))
# user_temp=input('what is the user feeling hot or cold?:').upper()
# choice=input('does the user want to make the choice YES or NO').upper()

# if (temp>=15 or user_temp=='COLD') and choice=='YES':
#     print('The user decided to increasse the temprature')

# elif (temp<=28  or user_temp=='HOT') and  choice=='YES':
#     print('user decided to cool down the ac') 

# else:
#     print('System dialing......')       

#checking if banned

# username=input('what is your username?:').upper()
# if not username.upper()=='TAGS' or username.upper()=='LAX':
#     print('welcome acsses granted')
# else:
#     print('sorry ur banned')    
 
# password='1234567'
# attempt=4


# for i in range(attempt):
#     password_gusse=input('What is your passowrd')
#     attempt-=1
#     if password==password_gusse:
#         print('you have gussed the passowrd')
#         break
#     else:
#         if not password==password_gusse:
#             print(f'sorry  u have this many attempts left {attempt}')
#     if attempt==0:
#         print('SORRY UR OUT OF ATTEMPTS') 

#gRADE BOUNDRIES WITH FOR LOOP

#for i in range(5):
    # grade_input = int(input('What is your grade?: '))

    # if grade_input < 0:
    #     print('unknown value')
    # elif grade_input >= 90:
    #     print('Final grade: A')
    # elif grade_input >= 80:
    #     print('Final Grade: B')
    # elif grade_input >= 70:
    #     print('Final Grade: C')
    # elif grade_input >= 60:
    #     print('Final Grade: D')
    # else:
    #     print('Final grade: F')

    # if input('would u like to exsit yes/no:?').upper() =='YES':
    #     break


#for loop database

# data_base=['TAGS069', 'CHUCK', 'LAX']
# password='12345'

# user_input=input('whatr is your username?').upper()

# if user_input in data_base:
#     for attempts in range(4):
#         password_input=input('what is ur password:')
#         if password_input==password:
#             print('congrats welcome')
#             break
#         else:
#             if not password_input==password:

#              print('sorry wrong password')
#     else:
#         print('out of attempts')
                  
# else:
#     print('username not found')

# while True:
#     user_input=input(('TYPE COMMAND TO ACCSES:')).upper()
#     if user_input=='ADMIN':
#         print('Welcome')
#         break
# print('try again')

#addition with for loop   
# total=0
# while True:
#     amount_added=int(input('what would u like to add'))
#     total+=amount_added
#     if input('Would u like to exsit yes or no:').upper()=='YES':
#         print(f'Your total is {total}')
#         break


#AC 2.0

# AC_temp=30

# while True:
#     user_choice=input('would u like  to cool down or turn up heat by 10C hot/cold:').upper()
#     if user_choice=='COLD':
#         constant=10
#         AC_temp-=constant
#     elif user_choice=='HOT':
#         constant=10
#         AC_temp+=constant    
#     else:
#         print('invlaid input')
#         continue    

#     if AC_temp <= 0:
#         print('WARNING: It is freezing in here!')
#     if AC_temp >= 50:
#         print('WARNING: It is dangerously hot!')

#     if input('Would u like to keep dialing yes or no:').upper()=='NO':
#         print(f'You have changed ur final temp to {AC_temp}')
#         break
    



# usernames = {
#       'TAGS069', 'CHUCK', 'LAX', 'DRAGON99', 'STEALTH_DEV', 
#       'CHUCK', 'SKYWALKER', 'IRON_MAIDEN', 'TAGS069', 'CODEMASTER',
#       'SHADOW_RUNNER', 'LAX', 'CYBER_PUNK', 'NEON_KNIGHT', 'STEALTH_DEV',
#       'GHOST_USER', 'ALPHA_OMEGA', 'CHUCK', 'VOID_WALKER', 'TAGS069',
#       'PHANTOM_X', 'NIGHT_OWL', 'CYBER_PUNK', 'TITAN_FALL', 'GHOST_USER'
#   }

# print('YOU HAVE CURRENTLY THIS MANY USERNAMES')

# for users,usernames in enumerate(usernames):
#     print(f'{users}.{usernames}' )




# Shopping cart program level 3 optimized
# items=[]
# prices=[]
# total=0
# tip_amount=0

# while True: #This asks for the items and its prices and adds it
#     food=input('What would u like to add to your cart or q to quit:').lower()
#     if food.lower()=='q':
#         tip=input('how much tip would u like to add tip yes or no:')
#         if tip=='no':
#             tip_amount=0
#             break
#         elif tip.lower()=='yes':
#             tip_amount=float(input('how much would u like to add:'))
#             break    


            

#     price=float(input('what is the price of this item:'))
      
#     items.append(food)
#     prices.append(price)
#     total=sum(prices)
    


# print('Your itemized Recipt:')



# seen = [] 

# for food, price in zip(items, prices): 
#     if food not in seen:
#         qty = items.count(food)
#         item_total = price * qty
#         print(f"{food.capitalize()} x{qty}: ${item_total:.2f}")
#         seen.append(food)




# vat=total*0.05
# new_total= total + vat +  tip_amount

# person_num_input=float(input('how many person are there to split:'))
# split_total=new_total/person_num_input



# print('--------------------')
# print(f'VAT added (5%): ${vat:.2f} and tipped: ${tip_amount:.2f}')
# print(f'Your total is: ${new_total:.2f}')
# print(f'your each fair share is {split_total:.2f}$')

#quiz game optimized level 2.5?
# questions = (
#     "Which Pokémon is known as the franchise mascot and 'Mouse Pokémon'?", 
#     "What is the capital city of Pakistan?", 
#     "Which scholar from the Islamic Golden Age is widely known as the 'Father of Algebra'?", 
#     "Which of the following is a classic Generation 1 Fire-type starter Pokémon?",
#     "In which city was the famous House of Wisdom located during the Islamic Golden Age?"
# )

# options = (
#     ("A. Eevee", "B. Pikachu", "C. Clefairy", "D. Meowth"),
#     ("A. Karachi", "B. Lahore", "C. Islamabad", "D. Peshawar"),
#     ("A. Ibn Sina", "B. Al-Khwarizmi", "C. Al-Razi", "D. Ibn Khaldun"),
#     ("A. Bulbasaur", "B. Squirtle", "C. Charmander", "D. Mudkip"),
#     ("A. Cairo", "B. Damascus", "C. Cordoba", "D. Baghdad")
# )

# answers = ("B", "C", "B", "C", "D")

# guesses = []
# score = 0
# question_num = 0

# for question, answer, option in zip(questions, answers, options):
#     print("-------")    
#     print(f"Q{question_num + 1}: {question}")
#     print("------------------------------------")
#     for x in option:
#         print(x)
    
#     while True:
#         user_selected_option = input("Please select an answer (A/B/C/D): ").upper()
#         if user_selected_option in ["A", "B", "C", "D"]:
#             break
#         print("Invalid choice. Please enter A, B, C, or D.")
    
#     print(f"You selected: {user_selected_option}")
#     guesses.append(user_selected_option)
    
#     if answer == user_selected_option:
#         print(" Correct")
#         score += 1
#     else:
#         print(f"Wrong Correct answer: {answer}")
    
#     question_num += 1

# print("#####################################")
# print("Your answers:", guesses)
# print("Correct answers:", answers)
# print(f"Your score is {score}/{len(questions)}")

#Dice roller lvl 2

# import random

# print("Welcome to the Dice Roller!")

# while True:
#     number_of_dice = int(input("How many dice do you want to roll? "))
    
#     total = 0
    
#     for i in range(number_of_dice):
#         roll = random.randint(1, 6)
#         print(f"Die {i + 1}: {roll}")
#         total = total + roll
        
#     print(f"Total: {total}")
    
#     play_again = input("Roll again? (y/n): ")
#     if play_again.lower() != "y":
#         print("Thanks for playing")
        # break

#login system lvl 2?
# entered_user = input("Enter username: ")
# entered_pass = input("Enter password: ")

# if entered_user == "admin" and entered_pass == "pokemon":
#     print("Login successful!")
# else:
#     print("Wrong username or password.")

# has_id = False
# has_ticket = True

# if has_id or has_ticket:
#     print("Welcome to the concert!")
# else:
#     print("You cannot enter without an ID or a ticket.")

# is_raining = True

# if not is_raining:
#     print("You can go play outside")
# else:
#     print("Stay inside, it is raining.")



# grass fire water pokemon rock paper sisccor game  lvl 2?

# import random

# rules = {
#     "Fire": "Grass",
#     "Water": "Fire",
#     "Grass": "Water"
# }

# player = input("Choose Fire, Water, or Grass: ")
# computer = random.choice(["Fire", "Water", "Grass"])

# print(f"Computer chose: {computer}")

# if player == computer:
#     print("It is a tie")
# elif rules[player] == computer:
#     print("You win!")
# else:
#     print("You lost")



#lvl 3 hangman(roblox art)
# import random

# words = ["pikachu", "eevee", "pakistan", "lahore", "islamabad", "baghdad", "algebra"]
# word = random.choice(words)
# guessed_letters = []
# lives = 6

# stages = [
#     r"""
#       +---+
#       |   |
#     [x_x] |
#    /[===]\ |
#     |   | |
#           |
#     =========
#     """,
#     r"""
#       +---+
#       |   |
#     [o_o] |
#    /[===]\ |
#     |     |
#           |
#     =========
#     """,
#     r"""
#       +---+
#       |   |
#     [o_o] |
#    /[===]\ |
#           |
#           |
#     =========
#     """,
#     r"""
#       +---+
#       |   |
#     [o_o] |
#    /[===] |
#           |
#           |
#     =========
#     """,
#     r"""
#       +---+
#       |   |
#     [o_o] |
#     [===] |
#           |
#           |
#     =========
#     """,
#     r"""
#       +---+
#       |   |
#     [o_o] |
#           |
#           |
#           |
#     =========
#     """,
#     r"""
#       +---+
#       |   |
#           |
#           |
#           |
#           |
#     =========
#     """
# ]

# while lives > 0:
#     print(stages[lives])
    
#     display_word = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display_word = display_word + letter + " "
#         else:
#             display_word = display_word + "_ "
            
#     print(display_word)
#     print("Guessed letters:", guessed_letters)
    
#     if "_" not in display_word:
#         print("congrats u svaed him lol ")
#         break
        
#     guess = input("Guess a letter: ").lower()
    
#     if len(guess) != 1 or not guess.isalpha():
#         print("cant enter more than 2 letter.")
#         continue
        
#     if guess in guessed_letters:
#         print("already gussed that ")
#         continue
        
#     guessed_letters.append(guess)
    
#     if guess in word:
#         print("Good guess!")
#     else:
#         print("Wrong guess!")
#         lives = lives - 1

# if lives == 0:
#     print(stages[0])
#     print("You lost :", word)



#slot machince lvl 3?
 
# import random 

# emojis = ["💀", "😭", "🙂‍↕️", "🔥"]

# balance = 100

# print("Welcome to the Emoji Slots!")

# while balance > 0:
#     print(f"Balance: ${balance}")
#     bet = int(input("Enter your bet: "))
    
#     if bet > balance:
#         print("You don't have enough money!")
#         continue
        
#     if bet <= 0:
#         print("Must bet more than 0!")
#         continue
        
#     balance = balance - bet
    
#     slot1 = random.choice(emojis)
#     slot2 = random.choice(emojis)
#     slot3 = random.choice(emojis)
    
#     print(f"\n[ {slot1} | {slot2} | {slot3} ]\n")
    
#     if slot1 == slot2 and slot2 == slot3:
#         winnings = bet * 10
#         print(f" JACKPOT! You won $:{winnings}")
#         balance = balance + winnings
#     elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
#         winnings = bet * 2
#         print(f" Match of 2 You won $:{winnings}")
#         balance = balance + winnings
#     else:
#         print("oops")
        
#     if balance <= 0:
#         print("Game Over! You ran out of money.")
#         break
        
#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         print(f"You walked away with ${balance}")
#         break

#slot machince lvl 4 re desgined with baking  one from above added
 
# import random

# emojis = ["💀", "😭", "🙂‍↕️", "🔥"]
# bank_balance = 100

# while True:
#     print("\n=== ATM & CASINO MENU ===")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Play Slot Machine")
#     print("5. Exit")
    
#     choice = input("Choose an option (1-5): ")
    
#     if choice == "1":
#         print(f"\nYour current balance is: ${bank_balance}")
        
#     elif choice == "2":
#         amount = int(input("\nEnter amount to deposit: "))
#         if amount > 0:
#             bank_balance = bank_balance + amount
#             print(f"Deposited ${amount}. New balance: ${bank_balance}")
#         else:
#             print("Invalid amount.")
            
#     elif choice == "3":
#         amount = int(input("\nEnter amount to withdraw: "))
#         if amount > bank_balance:
#             print("Insufficient funds.")
#         elif amount > 0:
#             bank_balance = bank_balance - amount
#             print(f"Withdrew ${amount}. Remaining balance: ${bank_balance}")
#         else:
#             print("Invalid amount.")
            
#     elif choice == "4":
#         balance = bank_balance
        
#         print("Welcome to the Emoji Slots.")
        
#         while balance > 0:
#             print(f"Balance: ${balance}")
#             bet = int(input("Enter your bet: "))
            
#             if bet > balance:
#                 print("You don't have enough money.")
#                 continue
                
#             if bet <= 0:
#                 print("Must bet more than 0.")
#                 continue
                
#             balance = balance - bet
            
#             slot1 = random.choice(emojis)
#             slot2 = random.choice(emojis)
#             slot3 = random.choice(emojis)
            
#             print(f"\n[ {slot1} | {slot2} | {slot3} ]\n")
            
#             if slot1 == slot2 and slot2 == slot3:
#                 winnings = bet * 10
#                 print(f" JACKPOT. You won $:{winnings}")
#                 balance = balance + winnings
#             elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
#                 winnings = bet * 2
#                 print(f" Match of 2 You won $:{winnings}")
#                 balance = balance + winnings
#             else:
#                 print("oops")
                
#             if balance <= 0:
#                 print("Game over. You ran out of money.")
#                 break
                
#             play_again = input("Play again? (y/n): ")
#             if play_again.lower() != "y":
#                 print(f"You walked away with ${balance}")
#                 break
                
#         bank_balance = balance
        
#     elif choice == "5":
#         print("\nThank you for using the ATM & Casino. Goodbye.")
#         break
#     else:
#         print("Invalid choice. Please select 1-5.")