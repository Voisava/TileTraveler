def move(px,py, dir):
    if "N" in dir:
        py += 1 
    elif "S" in dir:
        py -= 1
    elif "E" in dir:
        px += 1 
    elif "W" in dir:
        px -= 1 
    return px, py

def print_dir(position_x, position_y):
    # returns valid direction/s
    if position_x in [1, 2, 3] and position_y == 1:
        return "(N)orth."
    if position_x == 1 and position_y == 2:
        return "(N)orth or (E)ast or (S)outh."
    if position_x == 1 and position_y == 3:
        return "(E)ast or (S)outh."
    if position_x == position_y:
        return "(S)outh or (W)est."
    if position_x == 2 and position_y == 3:
        return "(E)ast or (W)est."
    if position_x == 3 and position_y == 2:
        return "(N)orth or (S)outh."

def valid_input(moves, user_input):
    # checks if input is valid
    moves = [x for x in moves]
    moves = list(filter(lambda x: 65 <= ord(x) <= 90, moves))
    #moves = ['N', 'E', 'S', 'W']
    return user_input in moves

position_x = 1
position_y = 1
print("You can travel:", print_dir(position_x, position_y))
while True:
    # if position (3,1) victory
    if position_x == 3 and position_y == 1:
        print("Victory!")
        break
    user_input = input("Direction: ")
    inp = user_input.upper()
    if valid_input(print_dir(position_x, position_y), inp):
        position_x, position_y = move(position_x, position_y, inp)
        if position_x == 3 and position_y == 1:
            print("Victory!")
            break
        else:
            print("You can travel:", print_dir(position_x, position_y))
    else:
        print("Not a valid direction!")
        print("You can travel:", print_dir(position_x, position_y))
