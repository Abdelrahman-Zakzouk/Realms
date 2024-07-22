# import needed modules
import time
import random


# creates a story telling like print function to simulate a story
def print_pause(str):
    print(str)
    time.sleep(0)


# point system for deciding the victory or defeat of the player
def points(pts):
    global score
    if pts > 0:
        print_pause(f"You are granted {pts} points!")
        score += pts
    elif pts < 0:
        print_pause(f"You are deducted {abs(pts)} points!")
        score += pts


# plays the intro storyline when called
def intro():
    print_pause(
        "You awaken in the Echoes of Eternity, a realm existing between dimensions, where the boundaries of reality are fluid and ever-changing. As a traveler marooned in this surreal plane, your mission is to navigate through its shifting pathways and resolve the mysteries of its fragmented worlds. Your choices and actions will be tracked by a point system that will determine your success or failure."
    )


# function for presenting the user with different decisions based on a certain situation
def decision(explanation, decision, str1, str2):
    print_pause(explanation)
    print_pause(decision)
    while True:
        try:
            global number
            number = int(
                input(
                    f"Choose the number corresponding to the decision you'd like to make.\n1: {str1}\n2: {str2}\n"
                )
            )
            if number in range(1, 3):
                break
            print("Input outside of range")
        except ValueError:
            print("Invalid input\n\n")


# function that assigns a function to be called based on the number the user decides on
def assign(action1, action2):
    match number:
        case 1:
            action1()
        case 2:
            action2()


# function to randomize the outcome of different decisions the player makes
def randomize(good_possibility, positive_points, bad_possibility, negative_points):
    possibilities = [good_possibility, bad_possibility]
    current_possibility = random.choice(possibilities)
    print_pause(current_possibility)
    if current_possibility == good_possibility:
        points(positive_points)
    else:
        points(negative_points)


# the story line that gets executed if the user selects path a
def path_A():
    print_pause(
        "Path A (Star Chart Maze): Navigate through the maze to find a hidden chamber."
    )
    print_pause(
        "Success (Path A): Successfully navigate the maze and discover a hidden chamber with a celestial key."
    )
    global key
    key = True
    points(10)


# the story line that gets executed if the user selects path b
def path_B():
    print_pause(
        "Path B (Dark Corridor): Take the corridor to avoid the maze but face potential dangers."
    )
    randomize(
        "Success: Proceed through the corridor without incident and find a room with an ancient astronomical tome.",
        10,
        "Failure (Path B): Encounter cosmic creatures that attack you. You take minor damage but reach the same destination the maze leads to.",
        -10,
    )


# the story line that gets executed if the user selects path b
def path_C():
    print_pause(
        "Path C (Unstable Celestial Device): Investigate the unknown area with the unstable celestial device."
    )
    randomize(
        "Success: Carefully approach and stabilize the celestial device, revealing a hidden mechanism that grants valuable insights.",
        20,
        "Failure (Path B): Encounter cosmic creatures that attack you. You take minor damage but reach the same destination the maze leads to.",
        -20,
    )


# the story line that gets executed if the user decides to complete the task
def complete_task():
    print_pause(
        "Complete the Task: Assist the sage in finding a lost artifact within the maze."
    )
    print_pause(
        "Success (Complete Task): Find the artifact and gain the sage’s guidance."
    )
    points(25)


# the story line that gets executed if the user decides to refuse the task
def refuse_task():
    print_pause("Refuse: Attempt to continue without the sage’s help.")
    print_pause(
        "Failure (Refuse): Struggle through the realm without the sage’s assistance."
    )
    points(-10)


# the story line that gets executed if the user decides to use the key
def use_key():
    if key:
        randomize(
            "Success: You solve the puzzle with the knowledge and items collected. Gain access to the exit portal and escape the Echoes of Eternity.",
            30,
            "Failure: Fail to solve the puzzle or misuse items, resulting in a complete loss of points and failure to escape.",
            -30,
        )
    else:
        print_pause("Key not acquired")
        points(-25)


# the story line that gets executed if the user decides not to use the key
def dont_use_key():
    print_pause(
        "Failure: Fail to solve the puzzle or misuse items, resulting in a complete loss of points and failure to escape."
    )
    global score
    score = 0


# function for restarting the game if wanted
def restart():
    global answer
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("Do you want to restart? y/n\n").lower()
        if answer == "n":
            return True
        elif answer == "y":
            return False
        else:
            print("Invalid response")


# display the result in points as well as win or loss terms
def result():
    if score >= 30:
        state = "win"
    else:
        state = "lose"
    print_pause(f"Total score: {score}.You {state}!")


# main code, resetting some variables and calling functions to run
while restart:
    try:
        key = False
        score = 0
        intro()
        decision(
            "You find yourself in a majestic observatory floating in space. The room is filled with enormous, rotating star charts and cosmic instruments. Glowing constellations and celestial maps are scattered around, hinting at hidden secrets.",
            "Use the ancient star map to navigate through the observatory. You see two paths: one leads through a maze of rotating star charts, and the other through a dark, narrow corridor.",
            "Path A",
            "Path B",
        )
        assign(path_A, path_B)
        decision(
            "After clearing the path you crossed, you meet an enigmatic sage who offers to guide you if you complete a task.",
            "",
            "Complete the Task: Assist the sage in finding a lost artifact within the maze",
            "Refuse: Attempt to continue without the sage’s help.",
        )
        assign(complete_task, refuse_task)
        print_pause(
            "You find a portal and enter it, you get teleported to the Nexus of Realities"
        )
        decision(
            "You Arrive at the Nexus of Realities, where the energies of the realms converge. Here, you face the ultimate challenge that tests everything you’ve learned and collected.",
            "Use the celestial key to solve a complex puzzle",
            "Use key",
            "Don't use key",
        )
        assign(use_key, dont_use_key)
        result()
        if restart():
            break

    # error handling
    except ValueError:
        print("Invalid input\n\n")
