
# from conf import *

# from game.utils.func import(
#     clear_screen,
#     move_down,
#     move_left,
#     move_right,
#     move_up,
#     is_door_nearby,
#     distance,
#     get_dragon_hear_direction,
#     get_dragon_smell_direction,
#     show_error,
#     detect_dragon_smell,
#     move_dragon_towards_player,
#     move_dragon_towards_player_if_heard,
#     get_valid_player_position_input
# )

# from game.helper.const import(
#     RUNNING,
#     GRID,
#     DOOR_POSITION,
#     DUNGEON_POSITION,
#     DRAGON_POSITION,
#     PLAYER_POSITION,
#     DRAGON_SMELL_DIRECTION
# )


# from game.helper.exception import(
#     DirectionNameError,
# )

# # ''' The execution function of the program '''
# # def main():
# #     print("Welcome to Dungeon and Dragon Game!")
# #     print("Find the dungeon or the door position to win the game.")
    
# def main():
#     print("Welcome to Dungeon and Dragon Game!")
#     print("Find the dungeon or the door position to win the game.")
    


#     ''' The loop corresponding to the player's position,dragon's position,
#     dungeon's position,door's position'''
#     while RUNNING:
#         for row in GRID:
#             for cell in row:
#                 if cell == PLAYER_POSITION:
#                     print("X", end="  ")
#                 elif cell == dragon_position:
#                     print("D", end="  ")
#                 elif is_door_nearby(PLAYER_POSITION, DOOR_POSITION) and cell == DOOR_POSITION:
#                     print("?", end="  ")    
#                 elif cell == DUNGEON_POSITION:
#                     print("O", end=" ")    
#                 else:
#                     print(".", end="  ")
#             print()
            
#         if PLAYER_POSITION == dragon_position:
#             print("Game over, you have been defeated by the dragon!")
#             break
#         elif PLAYER_POSITION == DUNGEON_POSITION:
#             print("Congratulations, you have reached the dungeon and won the game!")
#             break   
#         elif PLAYER_POSITION == DOOR_POSITION:
#             print("Congratulations, you have reached the door and won the game!")
#             break
            
#         direction = input("Enter a direction (up /down /left / right): ")
#         clear_screen()

#         ''' Call the appropriate move function based on the user's input '''
#         try:
#             if direction == "up":
#                 PLAYER_POSITION = move_up(PLAYER_POSITION)
#             elif direction == "down":
#                 PLAYER_POSITION = move_down(PLAYER_POSITION)
#             elif direction == "left":
#                 PLAYER_POSITION = move_left(PLAYER_POSITION)
#             elif direction == "right":
#                 PLAYER_POSITION = move_right(PLAYER_POSITION)
#             else:
#                 raise DirectionNameError()
#         except DirectionNameError as e:
#             logger.warning("User write invalid direction")
#             show_error("please Enter correct direction! ")
#         try:
#             player_x = int(input("Enter the x coordinate of your starting position (0-7): "))
#             player_y = int(input("Enter the y coordinate of your starting position (0-7): "))

#             if player_x < 0 or player_x > 7 or player_y < 0 or player_y > 7:
#                 raise ValueError()
#             break
#         except ValueError as e:
#             logger.warning(" User invalid coordinates ...")
#             print("-------------------")
#             print("Invalid coordinates! Please Enter correct values 'JUST' between 0 and 7.")
#             print("-------------------")

#     PLAYER_POSITION = (player_x, player_y)
#     dragon_position = (0, 0)
    



#     PLAYER_POSITION = get_valid_player_position_input
# new_position = move_up(PLAYER_POSITION)
# new_position = move_right(PLAYER_POSITION)
# new_position = move_left(PLAYER_POSITION)
# new_position = move_down(PLAYER_POSITION)
# new_position = move_dragon_towards_player(PLAYER_POSITION, DRAGON_POSITION, DRAGON_SMELL_DIRECTION)
# new_position = move_dragon_towards_player_if_heard(PLAYER_POSITION, DRAGON_POSITION)

# PLAYER_POSITION = (1, 1)
# DRAGON_POSITION = (3, 3)
# dragon_smell_direction = (-1, -1)

# new_dragon_position = move_dragon_towards_player(PLAYER_POSITION, DRAGON_POSITION, dragon_smell_direction)

# smell_direction = get_dragon_smell_direction(DRAGON_POSITION, PLAYER_POSITION)
# print(smell_direction)

# DRAGON_POSITION = (3, 3)
# PLAYER_POSITION = (1, 1)

# hear_direction = get_dragon_hear_direction(DRAGON_POSITION, PLAYER_POSITION)
# print(hear_direction)

# position1 = (1, 1)
# position2 = (4, 5)

# dist = distance(position1, position2)
# print(dist)

# DRAGON_POSITION = (3, 3)
# PLAYER_POSITION = (1, 1)

# result = detect_dragon_smell(DRAGON_POSITION, PLAYER_POSITION)
# if result is not None:
#     print(result)

    
    #     '''Check if the dragon can smell the player 3cells to player,
    #     and with 30% chance '''
    #     dragon_smell_direction = get_dragon_smell_direction(dragon_position, PLAYER_POSITION)
    #     if dragon_smell_direction != "unknown":
    #         dragon_smell_distance = abs(dragon_position[0] - PLAYER_POSITION[0]) + abs(dragon_position[1] - PLAYER_POSITION[1])
    #         if dragon_smell_distance <= 3:
    #             print("The dragon smells you from the", dragon_smell_direction)

                
    #             # With a 30% probability, move towards the player immediately
    #             if random.random() <= 0.3:
    #                 if dragon_smell_direction == "up":
    #                     dragon_position = move_up(dragon_position)
    #                 elif dragon_smell_direction == "down":
    #                     dragon_position = move_down(dragon_position)
    #                 elif dragon_smell_direction == "left":
    #                     dragon_position = move_left(dragon_position)
    #                 elif dragon_smell_direction == "right":
    #                     dragon_position = move_right(dragon_position)
    #                 print("The dragon moves towards you!")
    #         else:
    #             print("The dragon doesn't smell anything")
    #     else:
    #         print("The dragon doesn't smell anything")

    #     ''' Check if the dragon can hear the player and with 90% chance move to player '''
    #     dragon_hear_direction = get_dragon_hear_direction(dragon_position, PLAYER_POSITION)
    #     if dragon_hear_direction != "unknown":
    #         print("The dragon hears you from the", dragon_hear_direction)

    #         ''' With a 90% probability, move towards the player immediately '''
    #         if random.random() <= 0.9:
    #             if dragon_hear_direction == "up":
    #                 dragon_position = move_up(dragon_position)
    #             elif dragon_hear_direction == "down":
    #                 dragon_position = move_down(dragon_position)
    #             elif dragon_hear_direction == "left":
    #                 dragon_position = move_left(dragon_position)
    #             elif dragon_hear_direction == "right":
    #                 dragon_position = move_right(dragon_position)
    #             print("The dragon moves towards you!")
    #     else:
    #         print("The dragon doesn't hear anything")
    #         ''' Calculate the distance between the player's position and the dragon's position '''
    #         if distance(PLAYER_POSITION, dragon_position) == 1:
    #             print("The dragon is in one of the adjacent cells")
    #         else:
    #             print("The dragon is not in one of the adjacent cells")


from conf import *
from game.helper.const import (
    RUNNING,
    GRID, 
    DOOR_POSITION, 
    DUNGEON_POSITION, 
    DRAGON_POSITION, 
    PLAYER_POSITION, 
    DRAGON_SMELL_DIRECTION
)

from game.helper.exception import DirectionNameError

from game.utils.func import(
    clear_screen,
    move_down,
    move_left,
    move_right,
    move_up,
    is_door_nearby, 
    distance, 
    get_dragon_hear_direction, 
    get_dragon_smell_direction, 
    show_error, 
    detect_dragon_smell, 
    move_dragon_towards_player,
    move_dragon_towards_player_if_heard, 
    get_valid_player_position_input
)    

def display_game_grid():
    """Displays the game grid"""
    for row in GRID:
        for cell in row:
            if cell == PLAYER_POSITION:
                print("X", end="  ")
            elif cell == DRAGON_POSITION:
                print("D", end="  ")
            elif is_door_nearby(PLAYER_POSITION, DOOR_POSITION) and cell == DOOR_POSITION:
                print("?", end="  ")
            elif cell == DUNGEON_POSITION:
                print("O", end=" ")
            else:
                print(".", end="  ")
        print()

def play_game():
    """Plays the Dungeon and Dragon game"""
    print("Welcome to Dungeon and Dragon Game!")
    print("Find the dungeon or the door position to win the game.")
    while RUNNING:
        display_game_grid()
        if PLAYER_POSITION == DRAGON_POSITION:
            print("Game over, you have been defeated by the dragon!")
            break
        elif PLAYER_POSITION == DUNGEON_POSITION:
            print("Congratulations, you have reached the dungeon and won the game!")
            break
        elif PLAYER_POSITION == DOOR_POSITION:
            print("Congratulations, you have reached the door and won the game!")
            break
        direction = input("Enter a direction (up /down /left / right): ")
        clear_screen()
        try:
            if direction == "up":
                PLAYER_POSITION = move_up(PLAYER_POSITION)
            elif direction == "down":
                PLAYER_POSITION = move_down(PLAYER_POSITION)
            elif direction == "left":
                PLAYER_POSITION = move_left(PLAYER_POSITION)
            elif direction == "right":
                PLAYER_POSITION = move_right(PLAYER_POSITION)
            else:
                raise DirectionNameError()
        except DirectionNameError:
            logger.warning("User entered an invalid direction")
            show_error("Please enter a valid direction!")
    print("Thanks for playing the game!")

if __name__ == "__main__":
    play_game()



    