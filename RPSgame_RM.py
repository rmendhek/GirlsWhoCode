# Rishma Mendhekar
# Girls who Code Application
# This program is for a Rock, Paper, Scissors game which allows users to play against the computer.
# The user chooses a move to make from a menu of buttons and the computer's move is generated randomly.
# Written in Python 3.6.4

from random import*
from graphics import*

''' A function that draws buttons with text labels.
 Takes in the window the button will be displayed in, the bottom right corner,
 top left corner, and label of the button '''
def drawButton(gwin, pt1, pt2, words): 
    button = Rectangle(pt1, pt2) # create a rectangle based on points and set a blue color
    button.setFill("blue3") 
    button.draw(gwin)  # draw the rectangle in the window
    labelx = (pt1.getX() + pt2.getX())/2.0 
    labely = (pt1.getY() + pt2.getY())/2.0 # label x and y is the middle coordinate of the button
    label = Text(Point(labelx,labely),words) # position the label in the middle of the button
    label.setFill("white")
    label.draw(gwin) # color the label white and draw it in the window

''' A function that displays an icon and some text for each move played by the user or computer.
 Takes in the move being played, which player played it, the x-coordinate of the image and text,
 and the window in which to display the image and text.'''
def moveDisplay(move, player, pointX, window):
        moveImg = Image(Point(pointX,50), "icons/"+move+str(player)+".gif") # load the image based on which move was made
        moveImg.draw(window) # draw it in the window
        if player == 1: # for player 1 (the user)
            moveTxt = Text(Point(pointX, 35), "You played "+move+"!") # create text object indicating move
            moveTxt.setSize(16) # set text size
            moveTxt.draw(window) # display text in window
        else: # for player 2
            moveTxt = Text(Point(pointX, 35), "Player 2 played "+move+"!") # create text object indicating move
            moveTxt.setSize(16) # set text size
            moveTxt.draw(window) # display text in window

        return moveImg, moveTxt # return the image and text so it can be undrawn later

''' A function that determines and displays who won.
 Takes in the introduction, the moves each player played, and the window to display.'''
def winner(intro, intro2, p1move, p2move, window):
    # Undraw the introductory text
    intro.undraw()
    intro2.undraw()
    # Compare results of players
    # If player 1 plays rock:
    if p1move == "rock" and p2move == "rock":
        winText = Text(Point(50, 75), "It's a tie!") # set the text determining who won
    elif p1move == "rock" and p2move == "paper":
        winText = Text(Point(50, 75), "Player 2 wins!")
    elif p1move == "rock" and p2move == "scissors":
        winText = Text(Point(50, 75), "You win!")
        
    # If player 1 plays scissors:
    elif p1move == "scissors" and p2move == "scissors":
        winText = Text(Point(50, 75), "It was a tie!")
    elif p1move == "scissors" and p2move == "rock":
        winText = Text(Point(50, 75), "Player 2 wins!")
    elif p1move == "scissors" and p2move == "paper":
        winText = Text(Point(50, 75), "You win!")
        
    # If player 1 plays paper:
    elif p1move == "paper" and p2move == "paper":
        winText = Text(Point(50, 75), "It was a tie!")
    elif p1move == "paper" and p2move == "rock":
        winText = Text(Point(50, 75), "You win!")
    elif p1move == "paper" and p2move == "scissors":
       winText = Text(Point(50, 75), "Player 2 wins!")
       
    winText.setSize(36) # set the size of the text
    winText.draw(window) # display the results in the window

    return winText # return the text so it can be undrawn later

'''This function calls moveDisplay() and winner() to display the moves and the winner in the window
Takes in the intro text objects, players' moves, and window to display.'''
def RPSmoves(intro, intro2, player1move, player2move, window):
    # call moveDisplay() to display the icon and text for players 1 and 2
    p1img, p1txt = moveDisplay(player1move, 1, 20, window)
    p2img, p2txt = moveDisplay(player2move, 2, 80, window)

    # call winner() to determine who won and display it in the window
    winnerTxt = winner(intro, intro2, player1move, player2move, window)

    return p1img, p1txt, p2img, p2txt, winnerTxt # return the icons and all text to be undrawn later

'''This function undraws the icons and text in the window.
It takes in the icons for players 1 and 2's moves and the winner text.'''
def undraw(p1img, p1txt, p2img, p2txt, winnerTxt):
    p1img.undraw()
    p1txt.undraw()
    p2img.undraw()
    p2txt.undraw()
    winnerTxt.undraw()
    
def RPSgame():
    
    ### Create the graphics window ###
    # create window
    win = GraphWin("Rock Paper Scissors", 800,800)
    # set coordinates so that 0,0 is at bottom left corner
    win.setCoords(0,0,100,100)
    
    # create introduction text objects and displays them for player
    introTxt = Text(Point(50,75), "This is a game of Rock, Paper, Scissors. Press one of the buttons below to make a move!")
    introTxt2 = Text(Point(50, 70), "Press any buton below to play again and press 'Exit' to quit.")
    introTxt.draw(win)
    introTxt2.draw(win)

    # create buttons: rock, paper, scissors, and exit using drawButton function above
    drawButton(win, Point(25, 10), Point (35,15), "Rock")
    drawButton(win, Point(45, 10), Point (55,15), "Paper")
    drawButton(win, Point(65, 10), Point (75,15), "Scissors")
    drawButton(win, Point(85, 90), Point (95,95), "Exit")

    # initialize moves in a list
    moves = ["rock", "paper", "scissors"]

    # initialize blank variables for images
    p1img = Text(Point(0,0), "")
    p1txt = Text(Point(0,0), "")
    p2img = Text(Point(0,0), "")
    p2txt = Text(Point(0,0), "")
    winnerTxt = Text(Point(0,0), "")

    # get a mouse click from the user
    pt = win.getMouse()
    
    # while the exit button is not clicked, let the user play
    while not (pt.getX() >= 85 and pt.getX() <= 95 and pt.getY() >= 90 and pt.getY() <=95): 

        ### Get moves from both players ###

        # if user has clicked the "rock" button, call RPSmoves which saves their move
        # and generates the computer's move randomly. The third parameter in RPSmove
        # is the user's move, indexed from the "moves" list above. The fourth is the
        # computer's move and is indexed randomly from the "moves" list.
        if pt.getX() >= 25 and pt.getX() <= 35 and pt.getY() >= 10 and pt.getY() <=15:
            undraw(p1img, p1txt, p2img, p2txt, winnerTxt) # undraw any icons and text
            p1img, p1txt, p2img, p2txt, winnerTxt = RPSmoves(introTxt, introTxt2, moves[0], moves[randint(0,2)], win) # return text and icons from RPSmoves so they can be undrawn

        # if the user has cliced the "paper" button, call RPSmoves
        elif pt.getX() >= 45 and pt.getX() <= 55 and pt.getY() >= 10 and pt.getY() <=15:
            undraw(p1img, p1txt, p2img, p2txt, winnerTxt)
            p1img, p1txt, p2img, p2txt, winnerTxt = RPSmoves(introTxt, introTxt2, moves[1], moves[randint(0,2)], win)

        # if user has clicked the "scissor" button, call RPSmoves
        elif pt.getX() >= 65 and pt.getX() <= 75 and pt.getY() >= 10 and pt.getY() <=15:
            undraw(p1img, p1txt, p2img, p2txt, winnerTxt)
            p1img, p1txt, p2img, p2txt, winnerTxt = RPSmoves(introTxt, introTxt2, moves[2], moves[randint(0,2)], win)

        # get another mouse click from the user
        pt = win.getMouse()

    # if the user clicks "exit", close the window
    win.close()

RPSgame()

    
