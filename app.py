def startProgram():
    programRunning = True

    while(programRunning == True):
        print("Paste your script below and press 'Enter', or press '1' or 'stop' to exit the program")
        userInput = input()

        #Exit the program
        if (userInput.lower() == 'stop' or userInput == '1'):
            programRunning = False
            break

        print('\nYour input is:\n\n' + userInput)
        print('\nDo you want to proceed with the following script? Press "0" or "y" to proceed or "1" to exit the program')
        nextUserInput = input()

        #Exit the program
        if (nextUserInput.lower() == 'stop' or nextUserInput == '1'):
            programRunning = False
            break
        if (nextUserInput.lower() == 'y' or nextUserInput.lower() == 'yes' or nextUserInput == 1):
            #Proceed to enter parameters
            programRunning = False
        
    
startProgram()
    