        # # '''Check if the dragon can smell the player 3cells to player,
        # # and with 30% chance '''
        # dragon_smell_direction = get_dragon_smell_direction(DRAGON_POSITION, PLAYER_POSITION)
        # if dragon_smell_direction != "unknown":
        #     dragon_smell_distance = abs(DRAGON_POSITION[0] - PLAYER_POSITION[0]) + abs(DRAGON_POSITION[1] - PLAYER_POSITION[1])
        #     if dragon_smell_distance <= 3:
        #         print("The dragon smells you from the", dragon_smell_direction)

                
                # With a 30% probability, move towards the player immediately
        #         if random.random() <= 0.3:
        #             if dragon_smell_direction == "up":
        #                 DRAGON_POSITION = move_up(DRAGON_POSITION)
        #             elif dragon_smell_direction == "down":
        #                 DRAGON_POSITION = move_down(DRAGON_POSITION)
        #             elif dragon_smell_direction == "left":
        #                 DRAGON_POSITION = move_left(DRAGON_POSITION)
        #             elif dragon_smell_direction == "right":
        #                 DRAGON_POSITION = move_right(DRAGON_POSITION)
        #             print("The dragon moves towards you!")
        #     else:
        #         print("The dragon doesn't smell anything")
        # else:
        #     print("The dragon doesn't smell anything")

        # ''' Check if the dragon can hear the player and with 90% chance move to player '''
        # dragon_hear_direction = get_dragon_hear_direction(DRAGON_POSITION, PLAYER_POSITION)
        # if dragon_hear_direction != "unknown":
        #     print("The dragon hears you from the", dragon_hear_direction)

        #     # ''' With a 90% probability, move towards the player immediately '''
        #     if random.random() <= 0.9:
        #         if dragon_hear_direction == "up":
        #             DRAGON_POSITION = move_up(DRAGON_POSITION)
        #         elif dragon_hear_direction == "down":
        #             DRAGON_POSITION = move_down(DRAGON_POSITION)
        #         elif dragon_hear_direction == "left":
        #             DRAGON_POSITION = move_left(DRAGON_POSITION)
        #         elif dragon_hear_direction == "right":
        #             DRAGON_POSITION = move_right(DRAGON_POSITION)
        #         print("The dragon moves towards you!")
        # else:
        #     print("The dragon doesn't hear anything")
        #     # ''' Calculate the distance between the player's position and the dragon's position '''
        #     if distance(PLAYER_POSITION, DRAGON_POSITION) == 1:
        #         print("The dragon is in one of the adjacent cells")
        #     else:
        #         print("The dragon is not in one of the adjacent cells")
