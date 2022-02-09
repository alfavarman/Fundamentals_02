password = "tom yum"
guess = input("Guess Password: ")
guess_q = 1
guess_l = 3
guess_o = False

while guess != password and not(guess_o):
    if guess_q < guess_l:
        guess = input("Wrong Password Try Again: ")
        guess_q += 1
        print("input " + str(guess_q) + "of 3")
    else:
        guess_o = True


if guess_o:
    print("You typed wrong password 3 times. \n Account is locked now.")
else:
    print("Correct! You are in")


