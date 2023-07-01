# here will be the list of all the workout functions
import time


def abs():
    try:
        print("Ok, so what exercise you wanna choose?\n")
        time.sleep(2)
        workouts = {1: "Arms-High Partial Situp",
                    2: "Barbell Rollout",
                    3: "Swiss Ball Crunch",
                    4: "Dip/Leg Raise Combo",
                    5: "Flutter Kick",
                    6: "Leg Raise",
                    7: "Medicine Ball Russian Twist",
                    8: "Medicine Ball Mountain Climber",
                    9: "Pike to Superman",
                    10: "Plank"
                    }

        print("{:<2}-{:<2}".format('index ', ' Name'))
        for k, v in workouts.items():
            label = v
            print("{:<2}-{:<2}".format(k, label))

        time.sleep(1.5)
        x = int(input("pick a number from the list:"))
        time.sleep(1.5)
        print(f"That's great!\nYou chose: {workouts[x]}")

        reps = int(input("How many reps to do?\n"))
        sets = int(input("How many sets to do?\n"))
        calories = 1
        working = (reps * sets)

        for work in range(working):
            if work < working:
                work += 1
                calories = (working / 2)
            time.sleep(1.5)
            print("Working..")
            time.sleep(1.5)
            print("Working...")
            time.sleep(1.5)
            print("Done!")
            print(f"Congrats! you just did {working} reps!\nYou just burned {calories} calories!")
            return calories

        else:
            print(f"oops, let's try again ")
            abs()

    except ValueError:
        if ValueError:
            print(f"oops, let's try again ")
            abs()
