import random
def hangman():
    word= random.choices(['pugger','tiger','batman','lion','python','kalu','anabela','earth','superman','panda'])
    validletters ="abcdefghijklmnopqrstuvwxyz"
    turn = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "    
        if main == word:
            print(main)
            print("You win!")
            break
        print("Guess the word",main)
        guess = input()
        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()
        
        if guess not in word:
            turn = turn - 1   
            if turn == 9:
                print("9 turn left")
                print("--------")     
            if turn == 8:
                print("8 turn left")
                print("--------")
                print("   O   ")
            if turn == 7:
                print("7 turn left")
                print("--------")
                print("   O    ")
            if turn == 6:
                print("6 turn left")
                print("--------")
                print("   O    ")
                print("   |    ")
            if turn == 5:
                print("5 turn left")
                print("--------")
                print("   O    ")
                print("   |    ")
                print("  /     ")
            if turn == 4:
                print("4 turn left")
                print("--------")
                print("   O    ")
                print("   |    ")
                print("  / \   ")
            if turn == 3:
                print("3 turn left")
                print("--------")
                print(" \ O    ")
                print("   |    ")
                print("  / \   ")
            if turn == 2:
                print("2 turn left")
                print("--------")
                print(" \ O /| ")
                print("   |    ")
                print("  / \   ")
            if turn == 1:
                print("1 turn left")
                print("last breath")
                print("--------")
                print(" \ O_/| ")
                print("   |    ")
                print("  / \   ")
            if turn == 0:
                print("0 turn left")
                print("You lose")
                print("--------")
                print("   O_|  ")
                print("  /|\   ")
                print("  / \   ")
                break

name = input("Enter your name:-")
print("Welcome",name)
print("---------------------------------------------------")
print("Try to guess word in less than 10 atemepts")
hangman()
print()
