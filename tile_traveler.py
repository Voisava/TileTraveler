# make a move
# print directions for each move
# check if valid input
# loop while position x,y is not 3,1
# if x,y is  3,1 print victory and break
# else continue looping

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
    print("You can travel:", moves(position_x, position_y))

position_x = 1
position_y = 1
coins = 0
moves = 0
print("You can travel:", print_dir(position_x, position_y))
while True:
    # if position (3,1) victory
    if position_x == 3 and position_y == 1:
        print("Victory!")
        break
    user_input = input("Direction: ")
    inp = user_input.upper()
    moves += 1
    if valid_input(print_dir(position_x, position_y), inp):
        position_x, position_y = move(position_x, position_y, inp)
        if position_x == 3 and position_y == 1:
            print("Victory! Total coins {}. Moves {}.".format(coins, moves))
            break

        elif position_y == 2 or (position_x == 2 and position_y == 3):
            pull_lever = input("Pull a lever (y/n): ")
        
            if pull_lever == "y" or pull_lever == "Y":
                
                print("You received 1 coin, your total is now {}.".format(coins))
                coins += 1
            elif pull_lever == "n" or pull_lever == "N":
                print("You can travel:", print_dir(position_x, position_y))
            print("You can travel:", print_dir(position_x, position_y))
        else:
            print("You can travel:", print_dir(position_x, position_y))
    else:
        print("Not a valid direction!")
        print("You can travel:", print_dir(position_x, position_y))

    play_again = input("Play again (y/n):")
    if play_again != "y" or play_again != "Y":
        break
