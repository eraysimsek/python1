print("hello world") #display result 
import random #This provide function that generate random numbers and values.


def multiplication():   #defination for multiplacation calculation 
    
     x = input("Give me a number to multiply:") #input for first number 
     y = input("What do you want it multiplied by?") #input for second number 
     
     z =int(x) * int(y)  #calculate modulo operator
    
     print ("The result is: " + str(z)) #display result 
    
    
def division(): # defination of division operation
      x = input("give me a divident:") #input convert to integer according x
      y = input("What do you want it divided by?") # #input convert to integer according y
         
      z = float(x) / int(y)  #  integer division operation  
        
      print("The result is: " + str(z)) #print the result division operation
   
     
def wide_boy_string(): # defination of wide_boy_string operation
    user_str = input("Give me a string to w i d e n \n") #input and assign to user_str
    
    for char in user_str: # loop for each character in the user input
         print(char, end=" ") ## print the character without newline character followed by space

def wide_boy_string2(): # defination of wide_boy_string2 operation
    user_str = input ("give me a string to w i d e n \n") #input and assign to user_str
    
    i = 0 #counter i to zero
    
    wide_str = " "  #wide_str to a single space character
    
    for char in user_str : # loop over each character in the input

        wide_str = wide_str + char + " " # add the character followed space to wide_str
            
        if i < len(user_str) - 1: # check if the current character not the last character in the input
            wide_str = wide_str + char + " " # add the character followed space to wide_str
        else: # if the current character is  last character in  input
            wide_str = wide_str + char     
                # add  character without a space wide_str
        i += 1 # increment the counter
        
    print(wide_str) # print the widened string
    

def for_loop_example(): # defination of for_loop_example operation
    x = input("How many times should i run?") #input and assign to x
      
    for i in range(int(x)): # loop fnish the range of numbers from 0 to x1
        print("This loop is running for the " +str(i+1) +" time. ") # print message the current iteration number

    
def odd_or_even():# defination of odd_or_even operation
    x  = int(input("Which number do you want me to check?")) #enter a number and assign to x
        
    if x % 2 == 0: # check if the number is even

        print("The number" + str(x)+" is even ") # if even print this message
    else: # if not even, it must be odd
        print("The number" + str(x)+" is an odd duck. ") # print this message 
        
def ascii_sum():# defination of ascii_sum operation
    user_str = input("Give me a string for which you want the sum of the ASCII values of its chars: \n") #input a string and store it in user_str

    str_size = len(user_str) #length of the user_str string and store it in str_size
    
    i = 0 #Set i variable to 0
    
    sum=0 ## sum to 0 to store the total ASCII 
    
    while i < str_size: ## Loop each character in str 
        
        sum = sum + ord(user_str[i]) ## ASCII value of the current character and add it to the sum 
        i = i + 1 ## i by 1 move to the next character in the str
        
    print("The sum of all these ASCII values is" , str(sum)) ## Print the final sum of the ASCII values 
    

def string_flipper(): #defines the function called 
    user_str = input("Give me a string you want flipped or reversed \n") #  enter a string and stores 
    
    for char in reversed (user_str): #each character in the reversed of the str
        print(char, end="") #prints each character in the reversed string
        

def change_machine(): #defines the function called 
     change = int(input("how much do you want \n ")) # input an amount of money they want to receive 
     coins = (100,50,25,10,5) #use to calculate the amount of change to be given.
     coin_counts = [0,0,0,0,0] #will be used to keep track of the number of coins
     for i in range(len(coins)): # over each coin value in the coins 
         while change >= coins[i]:  #change required is greater than or equal to the value of the current coin.
           change -= coins[i] #coin from the remaining amount of change required.
           coin_counts[i] += 1 #Increases the count of the current coin in the coin_counts 
     print("Total number of coins:", sum(coin_counts)) # Prints the total number of coins
     print("Coin counts:", coin_counts) # Prints the total number of coins needed
                        

def rock_paper_scissors(): #defines the function called 
    options = ['rock', 'paper', 'scissors'] #this line creates a list of the options for the game
    player_choice = input("Choose rock, paper, or scissors: ").lower() #This line prompts the user to input their choic
    computer_choice = random.choice(options) #This line uses the randomly choice option 

    print("You chose:", player_choice) #This lines simply print out 
    print("Computer chose:", computer_choice) #This lines simply print out 

    if player_choice == computer_choice: #This line checks if the user choice  same as computer choic
        print("It's a tie!") #print  message indicating that it a tie.
        #Under this line shown, line checks if  choice beats the computer choice according to the game rules.
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!") # print a message  that the you win.
    else:
        print("Computer wins!") #print a message that the computer wins.


def Mario_wins():
    # Get user input for the number of stairs
    stairs = int(input("How many stairs should Mario climb to finish the level? "))

    # Check that the number of stairs is within range (1-23)
    if stairs < 1 or stairs > 23:
        print("Invalid number of stairs. Please choose a number between 1 and 23.")
        return

    # Loop through each row of the stairs pattern and print it
    for i in range(stairs):
        print(" " * (stairs - i - 1) + "#" * (i + 2) + "  |")

    # Print the base of the stairs
    print("#" * (stairs + 2) + "  |>")

# Define a function that displays a menu of options 
def menu():
    print("Please select a function to run by entering a number between 0 and 10:")
    print("0. Multiplication")
    print("1. Division")
    print("2. Wide Boy String")
    print("3. Wide Boy String 2")
    print("4. For Loop Example")
    print("5. Odd or Even")
    print("6. ASCII Sum")
    print("7. String Flipper")
    print("8. Change Machine")
    print("9. Rock Paper Scissors")
    print("10. Mario Wins")
    print("q. Quit")
    
# Loop indefinitely until  chooses to quit
while True:
    # Display the menu options 
    menu()
    # Prompt the user to enter a selection
    user_input = input("Enter selection: ")
    
    # If enters q, exit the program
    if user_input == "q":
        break
        
    # If enters an invalid selection, prompt them to enter again
    if user_input not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("Not a valid selection.")
        continue
    
    # Depending onselection, call a different function
    if user_input == "0":
        multiplication()
    elif user_input == "1":
        division()
    elif user_input == "2":
        wide_boy_string()
    elif user_input == "3":
        wide_boy_string2()
    elif user_input == "4":
        for_loop_example()
    elif user_input == "5":
        odd_or_even()
    elif user_input == "6":
        ascii_sum()
    elif user_input == "7":
        string_flipper()
    elif user_input == "8":
        change_machine()
    elif user_input == "9":
        rock_paper_scissors()
    elif user_input == "10":
        Mario_wins()