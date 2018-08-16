# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random #We'll need this later in the lab
import time

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 2

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []


#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)

for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos , y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp = snake.stamp()
    stamp_list.append(stamp)
snake.color("white")


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN=1
LEFT=2
RIGHT=3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

screen=turtle.Screen()
screen.bgcolor("black")
screen.title("snake")


def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")


direction = DOWN
def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    print("You pressed the down key!")    


direction = LEFT
def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    print("You pressed the left key!")


direction = RIGHT
def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    print("You pressed the right key!")



#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.listen()
turtle.onkeypress(down, DOWN_ARROW) # Create listener for up key
turtle.listen()
turtle.onkeypress(left, LEFT_ARROW) # Create listener for up key
turtle.listen()
turtle.onkeypress(right, RIGHT_ARROW) # Create listener for up key
turtle.listen()

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stampslist
    rand_food_pos=(food_x,food_y)
    food.goto(rand_food_pos)
    food_pos.append(rand_food_pos)
    trash=food.stamp()
    food_stamps.append(trash)
    food.hideturtle()

i=0
score=turtle.clone()
score.pencolor("red")
end=turtle.clone()
end.pencolor("red")

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    noeat=True
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos-SQUARE_SIZE)
        print("You moved down!")
    elif direction==UP:
        snake.goto(x_pos, y_pos+SQUARE_SIZE)
        print("You moved up!")

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        end.write("GAME OVER", font=("david", 75, "normal"), align=("center"))
        time.sleep(1)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the rleft edge! Game over!")
        end.write("GAME OVER", font=("david", 75, "normal"), align=("center"))
        time.sleep(1)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        end.write("GAME OVER", font=("david", 75, "normal"), align=("center"))
        time.sleep(1)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        end.write("GAME OVER", font=("david", 75, "normal"), align=("center"))
        time.sleep(1)
        quit()


    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
        print(food_stamps)                                       #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        noeat=False

        global i
        i+=1
        print(i)
        score.up()
        score.goto(350,-230)
        score.pendown()
        score.clear()
        score.write(i, font=("david", 20, "normal"))
        
        
    #HINT: This if statement may be useful for Part 8

    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    if noeat:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    if len(food_stamps) <= 100:
        make_food()

    turtle.ontimer(move_snake,TIME_STEP)

    if pos_list[-1] in pos_list[:-1]:
        print("you ate yourself")
        end.write("GAME OVER", font=("david", 75, "normal"), align=("center"))
        time.sleep(1)
        quit()

    if snake.pos() in rock_pos:
        print("you hit a rock!")
        end.write("GAME OVER", font=("david", 75, "normal"), align=("center"))
        time.sleep(1)
        quit()
    
        
        

     #<--- new line here

#Now, call the move_snake() function.  This starts moving the snake.  Once it starts 
#moving, it keeps moving by itself:


####################food##################

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
"""
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    trash=food.stamp()
    food_stamps.append(trash)
    food.hideturtle()
"""
rock_pos=[]

def make_rock():
    rock=turtle.clone()
    rock.shape("circle")
    rock.color("white")
    rock_stamps=[]
    global rock_pos

    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    rock_x = random.randint(min_x,max_x)*SQUARE_SIZE
    rock_y = random.randint(min_y,max_y)*SQUARE_SIZE

    rand_rock_pos=(rock_x,rock_y)
    rock.goto(rand_rock_pos)
    rock_pos.append(rand_rock_pos)
    rock_stamp=rock.stamp()
    rock_stamps.append(rock_stamp)
    rock.hideturtle()

    turtle.ontimer(make_rock,10000)


"""
def snake_change():
    snake_color["blue","red","yellow"]
    snake.color(snake_color)
    
turtle.ontimer(snake_change(),1000)
  """
        

make_rock()

start=turtle.clone()
start.pencolor("red")
end.write("READY?", font=("david", 75, "normal"), align=("center"))

time.sleep(1)
end.clear()
move_snake()
