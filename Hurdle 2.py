def turnRight():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()

for step in range(6):
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turnRight():
    turn_left()
    turn_left()
    turn_left()