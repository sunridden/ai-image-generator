import os
import replicate

# Directory where the app.py file is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create subdirectory generatedImgages in the same folder as app.py
save_directory = os.path.join(script_dir, "GeneratedImages")

#Ensure directoy exists, if not create it
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

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
        
def generateImage():

    input = {
        "prompt": "black forest gateau cake spelling out the words \"sun\", tasty, food photography, dynamic shot"
    }

    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input=input
    )

    for index, item in enumerate(output):
        save_path = os.path.join(save_directory, f"output_{index}.webp")
        with open(save_path, "wb") as file:
            file.write(item.read())
    #=> output_0.webp written to disk
    
#startProgram()
generateImage()
    