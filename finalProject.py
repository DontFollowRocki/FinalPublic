from tkinter import *
# creates window
root = Tk()
# determines title, image and size included in window
root.title('The Daily Muscle')
root.iconbitmap('muscle.ico')
root.geometry("700x500")

# defines the message when submitted
def submitClick():
    # allows the muscle group tag to be used in both windows
    global muscleGroup
    # defines messages given depending on area of body entered by user
    messages = {
        "Legs": "Great! Try doing 30 squats, 15 lunges and 25 mountain climbers!",
        "Upper Body": "Great! Try doing 25 wall push-ups, 30 butterflies and 1 minute of arm presses!",
        "Core": "Great! Try a 1 minute plank, 30 scissor kicks and 15 bicycles!"
    }
    # validation for user entered information allows for both upper and lower case responses
    # while creating an error if one of those specific responses are not entered
    message = messages.get(muscleGroup.get().title(), "Error. Please enter either legs, upper body or core.")
    # defines submit button
    submitMessage = Label(newWindow, text=message)
    submitMessage.grid(row=20, column=6)

# defines openWindowClick function
def openWindowClick():
    # using global allows use in both windows
    global newWindow
    global muscleGroup
    # defines the second window title, image and size
    newWindow = Toplevel(root)
    newWindow.title("Workout Window")
    newWindow.geometry("700x600")
    newWindow.iconbitmap('weight.ico')
    # message when new window is opened
    text = Label(newWindow, text="Fantastic! Let's get started! Choose the area of the body that you will be working on today. Legs, upper body or core?")
    # the area of the body entered by the user
    muscleGroup = Entry(newWindow, width=25, fg='black', bg='#e573ff')
    # defines submit button
    submitButton = Button(newWindow, text="Submit", command=submitClick, fg='black', bg='#e895f5', padx=25, pady=15)
    # defines exit button
    exitButton = Button(newWindow, text="Exit", command=exitClick, fg='black', bg='#e895f5', padx=25, pady=15)

    # defines grid placement of each 
    text.grid(row=0, column=6)
    muscleGroup.grid(row=15, column=6)
    submitButton.grid(row=18, column=6)
    exitButton.grid(row=35, column=6)

# exit function
def exitClick():
    exit()

# opening message
welcomeMessage = Label(root, text='Hello. Welcome to The Daily Muscle! ')
# opens second window when clicked
readyMessage = Label(root, text='Are you ready to get fit?')
yesButton = Button(root, text="Yes", command=openWindowClick, fg='black', bg='#e895f5', padx=25, pady=15)

# gets user name
nameMessage = Label(root, text="What is your name?")
nameEntry = Entry(root)
# defines grid placement
welcomeMessage.grid(row=0, column=6)
readyMessage.grid(row=4, column=6)
yesButton.grid(row=5, column=6)
nameMessage.grid(row=2, column=6)
nameEntry.grid(row=3, column=6)
# ends loop
root.mainloop()




