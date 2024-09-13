import  random
from copyreg import pickle
from logging import fatal

import  art
import game_data

data_a = {}
data_b = {}

previus_famous_people = []

player_score = 0
game_over = False
print(art.logo)
random_number_a = random.randint(0, len(game_data.data) -1)
while not game_over:

    random_number_b = random.randint(0, len(game_data.data) -1)
    
    if len(previus_famous_people)  <= 0:
        previus_famous_people.append(random_number_a)
        previus_famous_people.append(random_number_b)
        data_a = game_data.data[random_number_a]
        data_b = game_data.data[random_number_b]
    else:
        if random_number_b in previus_famous_people:
            while random_number_b in previus_famous_people:
                random_number_b = random.randint(0, len(game_data.data) - 1)
                data_b = game_data.data[random_number_b]
            previus_famous_people.append(random_number_b)
        else:
            data_b = game_data.data[random_number_b]
            previus_famous_people.append(random_number_b)



    print(f"Compare A: {data_a["name"]}, {data_a["description"]}, {data_a["country"]}.")
    print(art.vs)
    print(f"Againts B: {data_b["name"]}, {data_b["description"]}, {data_b["country"]}.")

    a_followers = data_a["follower_count"]
    b_followers = data_b["follower_count"]
    check_a_vs_b = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_a_vs_b == "a":
        if a_followers >= b_followers:
            player_score += 1
            print(art.logo)
            print(f"You're right! Current score: {player_score}")
            if player_score >= 49:
                print("You're the GOAT!")
                game_over = True
        else:
            game_over = True
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {player_score}")
    elif check_a_vs_b == "b":
        if b_followers >= a_followers:
            player_score += 1
            print(art.logo)
            print(f"You're right! Current score: {player_score}")
            data_a = data_b
            data_b = {}
            if player_score >= 49:
                print("You're the GOAT!")
                game_over = True
        else:
            game_over = True
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {player_score}")



