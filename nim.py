#I am a new to coding, so just tried my best to write this.  Any improvements to this code are much appreciated

balls=12
user=0
print ("Welcome to Dr. NIM's Lab. Lets play NIM's game \n RULES:\n There are total 12 balls, You and the computer both can only take balls upto 3 Max. \n And Whoever takes the last ball wins the Game, thats it! \n SIMPLE AF! \n")
print("Press Q and Hit ENTER to quit \n")
while user!='Q':
    user=input("YOUR TURN (Max.3) :  ")
    if user=='Q':
        print("YOU LOOOOSER!")
        break
    elif user=='q':
        print("YOU LOOOOSER!")
        break
    else:
        comp=4-(int(user))
        total=(int(comp)+int(user))
        balls=balls-total
        total+=total
        if int(user)>3:
            print("You can only take upto 3 balls, Try again \n")
            False
        else:
            print("\n Cool you took,",user,"balls. Now its Dr. NIM's Turn")
        
            print("NIM Took",comp,"balls \t Balls left:", balls,"\n")
            if balls==0:
                print("You lost, Dr. NIM took last ball, so he won, Try next time!")
                break
#Happy Coding