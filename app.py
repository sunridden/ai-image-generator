import os
import replicate
import math
import numpy as np

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

def splitScript(script):

    #Find number of images to produce
    print("How many images do you want to produce?")

    calculatedImages = False
    while(calculatedImages == False):
        imageNum = input()
        if imageNum.isdigit() == False:
            print("An integer must be given for the total number of images to produce")
        else:
            imageNum = int(imageNum)
            calculatedImages = True

    #Parses words in script into parts to convert to images
    scriptWords = script.split()

    # Splits evenly into parts based on the amount of images
    scriptParts = np.array_split(scriptWords, imageNum)

    # Combines each sub-array combining the words into a single string using ' '.join(...)
    newSplitScript = [' '.join(part) for part in scriptParts]
    
def calculateImageNum():
    # Calculates the number of images needed for a script given its word count, video length, and duration of each image
    
    print("How many words are in your script?")

    calculatedWords = False
    while(calculatedWords == False):
        wordCount = input()
        if wordCount.isdigit() == False:
            print("An integer must be given as the word count")
        else:
            wordCount = int(wordCount)
            calculatedWords = True

    print("How long is your script? (minutes)")

    calculatedMinutes = False
    while(calculatedMinutes == False):
        minuteCount = input()
        if minuteCount.isdigit() == False:
            print("An integer must be given as the script length count (minutes)")
        else:
            minuteCount = int(minuteCount)
            calculatedMinutes = True

    print("How long is your script? (seconds)")

    calculatedSeconds = False
    while(calculatedSeconds == False):
        secondCount = input()
        if secondCount.isdigit() == False:
            print("An integer must be given as the script length count (seconds)")
        else:
            secondCount = int(secondCount)
            calculatedSeconds = True

    print("How many seconds do you want each image to last? (Default is 10 seconds)")

    imageLength = False
    while(imageLength == False):
        imageLengthCount = input()
        if len(imageLengthCount) == 0:
            imageLengthCount = 10
            break
        if imageLengthCount.isdigit() == False:
            print("An integer must be given as the image length count (seconds)")
        else:
            imageLengthCount = int(imageLengthCount)
            imageLength = True

    videoLength = (minuteCount * 60) + secondCount

    totalImages = math.ceil(videoLength / imageLengthCount)

    wordsPerImage = math.ceil(wordCount / totalImages)

    print("There are " + str(totalImages) + " images with " + str(wordsPerImage) + " words per image")

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
#generateImage()
#calculateImageNum()