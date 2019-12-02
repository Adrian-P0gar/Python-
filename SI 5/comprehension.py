import random  # import random library

guesses_taken = 0  # guesses_taken is by default 0

# show the first message and request user input with his name
print('Hello! What is your name?')
myName = input()  # store the input with name of user

number = random.randint(1, 20)  ## choose a random number in range by 1 -20

# use the first input (user name) and print the second message
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6:  # condition for running time of the function
    print('Take a guess.')  # request a guess
    guess = input()  # store the guess input
    guess = int(guess)  # convert the input in integer

    ## change the count of guesses_taken, when this variable have count 5 while loop is stop
    guesses_taken += 1

    if guess < number:  # if the input is smaller than random choose number execut this code block
        print('Your guess is too low.')

    if guess > number:  # if the input is bigger than random choose number execut this code block
        print('Your guess is too high.')

    if guess == number:  # if the input is equal with random number stop the while loop
        break   # function for stop the code block (exit while loop)

if guess == number:  # when while loop is break verify the conditon for win. If input is equal with random number execut this block
    # convert user input in string for use it in next print
    guesses_taken = str(guesses_taken)
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken +
          ' guesses!')  # show the win message with name and taken number

if guess != number:  # when while loop is break verify the conditon for win. If input is not equal with random number execut this block
    # convert the random number in string for use it in next print
    number = str(number)
    print('Nope. The number I was thinking of was ' +
          number)   # print message for lose the game
