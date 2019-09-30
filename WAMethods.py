import tkinter as tk
from WorkoutAppGUI import *

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Creates the Main Label
def create_main_label(window, label):
    window.main_label = tk.Label(window, text=label,
                               font=font.Font(family='Helvetica', size=28, weight="bold", slant="italic"))
    window.main_label.pack(side="top", fill="x", pady=15)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Pick An Exercise Sequence

def pick_an_exercise(window, push_list, pull_list, legs_list, exercise_option):
    window.muscles = {"Push": ["Chest", "Shoulders", "Triceps"],
                    "Pull": ["Middle Back", "Lower Back", "Lats", "Biceps"],
                    "Legs": ["Quads", "Hamstrings", "Calves"]}
    window.group_label = tk.Label(window, text="Which Muscle Group?")
    window.group_label.pack()

    window.group_name = tk.StringVar(window)
    window.group_choices = ["Push", "Pull", "Legs"]
    window.group_menu = tk.OptionMenu(window, window.group_name, *window.group_choices)
    window.group_name.set("Push")
    window.group_menu.pack(pady=10)

    # /////////
    window.muscle_label = tk.Label(window, text="Which Muscle?")
    window.muscle_label.pack()

    window.muscle_name = tk.StringVar(window)
    window.muscle_choices = [muscle for muscle in window.muscles[window.group_name.get()]]
    window.muscle_name.set(window.muscle_choices[0])
    window.muscle_menu = tk.OptionMenu(window, window.muscle_name, *window.muscle_choices)
    window.muscle_menu.pack(pady=10)

    window.group_name.trace('w', lambda *args: update_muscles(window))

    # /////////
    if exercise_option:
        window.exercise_label = tk.Label(window, text="Which Exercise?")
        window.exercise_label.pack()

        window.exercise_name = tk.StringVar(window)
        if push_list["Chest"]:
            window.exercise_choices = [exercise for exercise in push_list["Chest"]]
        else:
            window.exercise_choices = ["None"]
        window.exercise_name.set("None")
        window.exercise_menu = tk.OptionMenu(window, window.exercise_name, *window.exercise_choices)
        window.exercise_menu.pack(pady=10)

        window.muscle_name.trace('w', lambda *args: update_exercises(window, push_list, pull_list, legs_list))

def update_muscles(window, *args):
    new_muscles = window.muscles[window.group_name.get()]
    window.muscle_name.set(new_muscles[0])

    menu = window.muscle_menu["menu"]
    menu.delete(0, 'end')

    for muscle in new_muscles:
        menu.add_command(label=muscle, command=lambda group=muscle: window.muscle_name.set(group))

def update_exercises(window, push_list, pull_list, legs_list):

    if window.muscle_name.get() in push_list:
        group = push_list
    elif window.muscle_name.get() in pull_list:
        group = pull_list
    else:
        group = legs_list

    new_exercises = group[window.muscle_name.get()]
    window.exercise_name.set("None")

    menu = window.exercise_menu["menu"]
    menu.delete(0, 'end')

    if new_exercises:
        for exercise in new_exercises:
            menu.add_command(label=exercise, command=lambda muscle=exercise: window.exercise_name.set(muscle))
    else:
        menu.add_command(label="None")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Returns the Muscle Group

def get_muscle_group(group_name, push_list, pull_list, legs_list):
    if group_name == "Push":
        return push_list
    elif group_name == "Pull":
        return pull_list
    else:
        return legs_list