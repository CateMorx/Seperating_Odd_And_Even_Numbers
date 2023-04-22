#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 3 
#Problem 1: Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt.
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.



#Imports necessary elements
import PySimpleGUI as psg
import time

#Creates Method For Separating Odd and Even Numbers From A text file containing 20 integers
def process():
    #Opens and creates the 3 files, "numbers.txt","even.txt","odd.txt"
    with open ("numbers.txt") as initial_file, open ("even.txt", "a") as even_numbers, open ("odd.txt", "a") as odd_numbers:

    #Reads each line in the "numbers.txt"
        for line in initial_file:
            number_line = int(line)

        #Determines if Even number and appends the value unto the "even.txt" file
        if number_line % 2 == 0:
                    even_lines=str(number_line)
                    even_numbers.write(even_lines + "\n")

        #Determines if Odd number and appends the value unto the "odd.txt" file
        else:
                    odd_lines=str(number_line)
                    odd_numbers.write(odd_lines + "\n")

#Creates a Method to Display the contents of the "numbers.txt" file using GUI
def GUI_1():
       
    #Opens and reads the "numbers.txt" file
    with open("numbers.txt", "r") as read_file:
        output_text = read_file.read()

    #Instantiates the color for the animated gradient effect of the GUI
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    
    # Create the PySimpleGUI window
    layout = [
        [psg.Column([
            [psg.Graph((800, 600), (0, 0), (800, 600), background_color='black', key='graph')],
        ], scrollable=True)]
    ]
    window = psg.Window("Initial Number Input", layout, finalize=True)

    # Get a reference to the Graph widget
    graph = window['graph']

     # Loop indefinitely to create the animated gradient effect
    while True:
        for i in range(len(colors)):
            for j in range(0, 360, 10):
                # Draw a rectangle with the current color and angle
                graph.DrawRectangle((0,0), (800,600), line_color='black', fill_color=colors[i])
                # Draw the output text on the graph widget
                graph.DrawText(output_text, (50, 240), color='black', font=('Helvetica', 16))
                # Add a short delay to slow down the animation
                time.sleep(0.01)
                # Update the PySimpleGUI window to show the new rectangle and text
                window.Refresh()
        event = window.read()
        #If window is closed, the loop ends
        if event == psg.WINDOW_CLOSED:
            window.close()
            break


#Creates a Method to Display the contents of the "even.txt" file using GUI
def GUI_2():
    #Opens and reads the "even.txt" file
    with open("even.txt", "r") as read_file:
        output_text = read_file.read()

    #Instantiates the color for the animated gradient effect of the GUI
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    # Create the PySimpleGUI window
    layout = [
        [psg.Column([
            [psg.Graph((800, 600), (0, 0), (800, 600), background_color='black', key='graph')],
        ], scrollable=True)]
    ]
    window = psg.Window("Initial Number Input", layout, finalize=True)

    # Get a reference to the Graph widget
    graph = window['graph']

    # Loop indefinitely to create the animated gradient effect
    while True:
        for i in range(len(colors)):
            for j in range(0, 360, 10):
                # Draw a rectangle with the current color and angle
                graph.DrawRectangle((0,0), (800,600), line_color='black', fill_color=colors[i])
                
                # Draw the output text on the graph widget
                graph.DrawText(output_text, (50, 240), color='black', font=('Helvetica', 16))

                # Add a short delay to slow down the animation
                time.sleep(0.01)
                # Update the PySimpleGUI window to show the new rectangle and text
                window.Refresh()

        event = window.read()
        #If window is closed, the loop ends
        if event == psg.WINDOW_CLOSED:
            window.close()
            break

#Creates a Method to Display the contents of the "odd.txt" file using GUI
def GUI_3():
    #Opens and reads the "odd.txt" file
    with open("odd.txt", "r") as read_file:
        output_text = read_file.read()
    #Instantiates the color for the animated gradient effect of the GUI
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    # Create the PySimpleGUI window
    layout = [
        [psg.Column([
            [psg.Graph((800, 600), (0, 0), (800, 600), background_color='black', key='graph')],
        ], scrollable=True)]
    ]
    window = psg.Window("Initial Number Input", layout, finalize=True)
    # Get a reference to the Graph widget
    graph = window['graph']
    # Loop indefinitely to create the animated gradient effect
    while True:
        for i in range(len(colors)):
            for j in range(0, 360, 10):
                # Draw a rectangle with the current color and angle
                graph.DrawRectangle((0,0), (800,600), line_color='black', fill_color=colors[i])
                
                # Draw the output text on the graph widget
                graph.DrawText(output_text, (50, 240), color='black', font=('Helvetica', 16))

                # Add a short delay to slow down the animation
                time.sleep(0.01)
                # Update the PySimpleGUI window to show the new rectangle and text
                window.Refresh()

        event = window.read()
        #If window is closed, the loop ends
        if event == psg.WINDOW_CLOSED:
            window.close()
            break

#Calls the proccess method
#Calls the First GUI method
#Calls the Second GUI method
#Calls the Third GUI method