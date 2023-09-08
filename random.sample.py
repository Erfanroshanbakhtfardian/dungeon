

        # # Move the dragon
        # if is_nearby(player_position, dragon_position):
        #     possible_directions = []
        #     if dragon_position[0] > 0:
        #         possible_directions.append("left")
        #     if dragon_position[0] < 7:
        #         possible_directions.append("right")
        #     if dragon_position[1] > 0:
        #         possible_directions.append("up")
        #     if dragon_position[1] < 7:
        #         possible_directions.append("down")
                
        #     directions_to_check = random.sample(possible_directions, int(len(possible_directions) * 0.3))
        #     for direction in directions_to_check:
        #         if direction == "up" and dragon_position[1] > player_position[1]:
        #             dragon_position = move_up(dragon_position)
        #             print("The dragon moves towards you!")
        #             break
        #         elif direction == "down" and dragon_position[1] < player_position[1]:
        #             dragon_position = move_down(dragon_position)
        #             print("The dragon moves towards you!")
        #             break
        #         elif direction == "left" and dragon_position[0] > player_position[0]:
        #             dragon_position = move_left(dragon_position)
        #             print("The dragon moves towards you!")
        #             break
        #         elif direction == "right" and dragon_position[0] < player_position[0]:
        #             dragon_position = move_right(dragon_position)
        #             print("The dragon moves towards you!")
        #             break
        #     else:
        #         print("The dragon doesn't smell anything")
        # else:
        #     print("The dragon doesn't smell anything")