# here is the main page of the App.
import time

"""here we configure what area of the body
the user want to do"""
print("what area you want to train today?\n")
time.sleep(1.5)

areas = {1: "Chest",
         2: "Back",
         3: "Legs",
         4: "Shoulders",
         5: "Hands",
         6: "Abs"
         }

print("{:<2}-{:<2}".format('index ', ' Workout-Name'))
for k, v in areas.items():
    label = v
    print("{:<2}-{:<2}".format(k, label))

