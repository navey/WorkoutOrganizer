import tkinter as tk
from tkinter import messagebox
from tkinter import font

import WAMethods


class AppDriver(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Naveen's Workout Organizer")
        tk.Tk.wm_geometry(self, "600x575")
        tk.Tk.wm_resizable(self, False, False)

        self.container = tk.Frame(self)
        self.container.pack()

        self.frames = {}
        for page in (MainMenu, ViewExercises, AddExercisePageOne, AddExercisePageTwo, AddExercisePageThree,
                     RemoveExercise, ModifyMenu, ChangeName, ChangeMusclePageOne, ChangeMusclePageTwo, Settings,
                     AddEquipment, RemoveEquipment, Load, Save):
            frame = page(parent=self.container, controller=self)
            self.frames[page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def refresh_all(self):
        for page in (ViewExercises, AddExercisePageOne, AddExercisePageTwo, AddExercisePageThree,
                     RemoveExercise, ChangeName, ChangeMusclePageOne, ChangeMusclePageTwo, AddEquipment,
                     RemoveEquipment):
            frame = page(parent=self.container, controller=self)
            self.frames[page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def refresh_view(self):
        self.frames["ViewExercises"] = ViewExercises(parent=self.container, controller=self)
        self.frames["ViewExercises"].grid(row=0, column=0, sticky="nsew")

    def refresh_add_exercise(self):
        self.frames["AddExercisePageOne"] = AddExercisePageOne(parent=self.container, controller=self)
        self.frames["AddExercisePageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["AddExercisePageTwo"] = AddExercisePageTwo(parent=self.container, controller=self)
        self.frames["AddExercisePageTwo"].grid(row=0, column=0, sticky="nsew")
        self.frames["AddExercisePageThree"] = AddExercisePageThree(parent=self.container, controller=self)
        self.frames["AddExercisePageThree"].grid(row=0, column=0, sticky="nsew")

    def refresh_remove_exercise(self):
        self.frames["RemoveExercise"] = RemoveExercise(parent=self.container, controller=self)
        self.frames["RemoveExercise"].grid(row=0, column=0, sticky="nsew")

    def refresh_change_name(self):
        self.frames["ChangeName"] = ChangeName(parent=self.container, controller=self)
        self.frames["ChangeName"].grid(row=0, column=0, sticky="nsew")

    def refresh_change_muscle(self):
        self.frames["ChangeMusclePageOne"] = ChangeMusclePageOne(parent=self.container, controller=self)
        self.frames["ChangeMusclePageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["ChangeMusclePageTwo"] = ChangeMusclePageTwo(parent=self.container, controller=self)
        self.frames["ChangeMusclePageTwo"].grid(row=0, column=0, sticky="nsew")

    def refresh_save(self):
        self.frames["Save"] = Save(parent=self.container, controller=self)
        self.frames["Save"].grid(row=0, column=0, sticky="nsew")


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.main_label = tk.Label(self, text="Main Menu",
                                   font=font.Font(family='Helvetica', size=48, weight="bold"))
        self.main_label.pack(side="top", fill="x", pady=15)

        self.view_list_but = tk.Button(self, text="View Exercises",
                                       command=lambda: self.controller.show_frame("ViewExercises"), width=20, height=3)
        self.add_exercise_but = tk.Button(self, text="Add Exercise",
                                          command=lambda: self.controller.show_frame("AddExercisePageOne"), width=20,
                                          height=3)
        self.remove_exercise_but = tk.Button(self, text="Remove Exercise",
                                             command=lambda: self.controller.show_frame("RemoveExercise"), width=20,
                                             height=3)
        self.modify_exercise_but = tk.Button(self, text="Modify Exercise",
                                             command=lambda: self.controller.show_frame("ModifyMenu"), width=20,
                                             height=3)
        self.settings_but = tk.Button(self, text="Settings", command=lambda: self.controller.show_frame("Settings"),
                                      width = 20, height=3)
        self.load_but = tk.Button(self, text="Load Save File",
                                  command=lambda: self.controller.show_frame("Load"), width=20, height=3)
        self.save_but = tk.Button(self, text="Save",
                                  command=lambda: self.controller.show_frame("Save"), width=20, height=3)

        self.view_list_but.pack(pady=5)
        self.add_exercise_but.pack(pady=5)
        self.remove_exercise_but.pack(pady=5)
        self.modify_exercise_but.pack(pady=5)
        self.settings_but.pack(pady=5)
        self.load_but.pack(pady=5)
        self.save_but.pack(pady=5)


class ViewExercises(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Exercises")

        self.view_list(self)

        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.controller.show_frame("MainMenu"), width=20,
                                  height=3)
        self.exit_but.pack(pady=10)

    @staticmethod
    def view_list(window):
        scrollbar_y = tk.Scrollbar(window)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        # scrollbarX = tk.Scrollbar(window)
        # scrollbarX.pack(fill=tkinter.X)
        text = tk.Text(window, yscrollcommand=scrollbar_y.set, font=font.Font(size=13, weight="bold"), width=50,
                       height=23)

        text.insert(tk.INSERT, "Push Muscles")
        for muscle in push_list:
            text.insert(tk.INSERT, "\n - " + muscle)
            for exercise in push_list[muscle]:
                text.insert(tk.INSERT, "\n   + " + push_list[muscle][exercise].get_name())
                if push_list[muscle][exercise].get_equipment()[0] != "None":
                    for equipment in push_list[muscle][exercise].get_equipment():
                        text.insert(tk.INSERT, "\n     * " + equipment)
                if push_list[muscle][exercise].get_reference()[0] != "None":
                    for reference in push_list[muscle][exercise].get_reference():
                        text.insert(tk.INSERT, "\n     # " + reference)

        text.insert(tk.INSERT, "\nPull Muscles")
        for muscle in pull_list:
            text.insert(tk.INSERT, "\n - " + muscle)
            for exercise in pull_list[muscle]:
                text.insert(tk.INSERT, "\n   + " + pull_list[muscle][exercise].get_name())
                if pull_list[muscle][exercise].get_equipment()[0] != "None":
                    for equipment in pull_list[muscle][exercise].get_equipment():
                        text.insert(tk.INSERT, "\n     * " + equipment)
                if pull_list[muscle][exercise].get_reference()[0] != "None":
                    for reference in pull_list[muscle][exercise].get_reference():
                        text.insert(tk.INSERT, "\n     # " + reference)

        text.insert(tk.INSERT, "\nLeg Muscles")
        for muscle in legs_list:
            text.insert(tk.INSERT, "\n - " + muscle)
            for exercise in legs_list[muscle]:
                text.insert(tk.INSERT, "\n   + " + legs_list[muscle][exercise].get_name())
                if legs_list[muscle][exercise].get_equipment()[0] != "None":
                    for equipment in legs_list[muscle][exercise].get_equipment():
                        text.insert(tk.INSERT, "\n     * " + equipment)
                if legs_list[muscle][exercise].get_reference()[0] != "None":
                    for reference in legs_list[muscle][exercise].get_reference():
                        text.insert(tk.INSERT, "\n     # " + reference)

        text.config(state=tk.DISABLED)
        text.pack()


class AddExercisePageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.error_message = False

        WAMethods.create_main_label(self, "Add Exercise")

        # /////////
        self.exercise_label = tk.Label(self, text="Name of Exercise?")
        self.exercise_label.pack()
        self.exercise_entry = tk.Entry(self)
        self.exercise_entry.pack(pady=20)

        # /////////
        WAMethods.pick_an_exercise(self, push_list, pull_list, legs_list, False)

        # /////////
        self.error_label = tk.Label(self, text="Please enter a name for the exercise before submitting")

        # /////////
        self.next_but = tk.Button(self, text="Next", command=lambda: self.check(), width=20, height=3)
        self.next_but.pack(pady=5)

        # /////////
        self.exit_but = tk.Button(self, text="Exit", command=self.exit, width=20, height=3)
        self.exit_but.pack(pady=5)

    def check(self):
        if not any(self.exercise_entry.get()) and not self.error_message:
            self.error_label.pack()
            self.error_message = True
        elif any(self.exercise_entry.get()):
            self.controller.show_frame("AddExercisePageTwo")

    def exit(self):
        self.controller.refresh_add_exercise()
        self.controller.show_frame("MainMenu")


class AddExercisePageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Add Exercise")

        self.equip1_label = tk.Label(self, text="Equipment One: ")
        self.equip1_label.pack()
        self.equip1_entry = tk.Entry(self)
        self.equip1_entry.pack(pady=10)

        self.equip2_label = tk.Label(self, text="Equipment Two: ")
        self.equip2_label.pack()
        self.equip2_entry = tk.Entry(self)
        self.equip2_entry.pack(pady=10)

        self.equip3_label = tk.Label(self, text="Equipment Three: ")
        self.equip3_label.pack()
        self.equip3_entry = tk.Entry(self)
        self.equip3_entry.pack(pady=10)

        self.equip4_label = tk.Label(self, text="Equipment Four: ")
        self.equip4_label.pack()
        self.equip4_entry = tk.Entry(self)
        self.equip4_entry.pack(pady=10)

        # /////////
        self.next_but = tk.Button(self, text="Next", command=lambda: self.controller.show_frame("AddExercisePageThree"),
                                  width=20, height=3)
        self.next_but.pack(pady=5)

        # /////////
        self.exit_but = tk.Button(self, text="Exit", command=self.exit, width=20, height=3)
        self.exit_but.pack(pady=5)

    def exit(self):
        self.controller.refresh_add_exercise()
        self.controller.show_frame("MainMenu")


class AddExercisePageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Add Exercise")

        self.url1_label = tk.Label(self, text="Reference Link One: ")
        self.url1_label.pack()
        self.url1_entry = tk.Entry(self)
        self.url1_entry.pack(pady=10)

        self.url2_label = tk.Label(self, text="Reference Link Two: ")
        self.url2_label.pack()
        self.url2_entry = tk.Entry(self)
        self.url2_entry.pack(pady=10)

        self.url3_label = tk.Label(self, text="Reference Link Three: ")
        self.url3_label.pack()
        self.url3_entry = tk.Entry(self)
        self.url3_entry.pack(pady=10)

        # /////////
        self.next_but = tk.Button(self, text="Next", command=self.add_exercise, width=20, height=3)
        self.next_but.pack(pady=5)

        # /////////
        self.exit_but = tk.Button(self, text="Exit", command=self.exit, width=20, height=3)
        self.exit_but.pack(pady=5)

    def add_exercise(self):
        muscle_group = WAMethods.get_muscle_group(self.controller.frames["AddExercisePageOne"].group_name.get(),
                                  push_list, pull_list, legs_list)
        muscle_name = self.controller.frames["AddExercisePageOne"].muscle_name.get()
        exercise_name = self.controller.frames["AddExercisePageOne"].exercise_entry.get()


        equipment = []
        page_two = self.controller.frames["AddExercisePageTwo"]
        if any(page_two.equip1_entry.get()):
            equipment.append(page_two.equip1_entry.get())
        if any(page_two.equip2_entry.get()):
            equipment.append(page_two.equip2_entry.get())
        if any(page_two.equip3_entry.get()):
            equipment.append(page_two.equip3_entry.get())
        if any(page_two.equip4_entry.get()):
            equipment.append(page_two.equip4_entry.get())

        reference = []
        if any(self.url1_entry.get()):
            reference.append(self.url1_entry.get())
        if any(self.url2_entry.get()):
            reference.append(self.url2_entry.get())
        if any(self.url3_entry.get()):
            reference.append(self.url3_entry.get())

        muscle_group[muscle_name][exercise_name] = Exercise(exercise_name, muscle_name, equipment, reference)
        master_list[exercise_name] = muscle_group[muscle_name][exercise_name]

        self.controller.refresh_all()
        self.controller.show_frame("ViewExercises")

    def exit(self):
        self.controller.refresh_add_exercise()
        self.controller.show_frame("MainMenu")


class RemoveExercise(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.error_message = False

        WAMethods.create_main_label(self, "Remove Exercise")

        WAMethods.pick_an_exercise(self, push_list, pull_list, legs_list, True)

        self.error_label = tk.Label(self, text="Please Select an Exercise Before Submitting")

        self.next_but = tk.Button(self, text="Next", command=lambda: self.check(), width=20, height=3)
        self.next_but.pack(pady=5)

        self.exit_but = tk.Button(self, text="Exit", command=self.exit, width=20, height=3)
        self.exit_but.pack(pady=10)

    def check(self):
        if self.exercise_name.get() == "None" and not self.error_message:
            self.error_label.pack()
            self.error_message = True
        elif self.exercise_name.get() != "None":
            self.remove_exercise()

    def remove_exercise(self):
        muscle_group = WAMethods.get_muscle_group(self.group_name.get(), push_list, pull_list, legs_list)

        muscle_group[self.muscle_name.get()].pop(self.exercise_name.get())
        master_list.pop(self.exercise_name.get())

        self.controller.refresh_all()
        self.controller.show_frame("RemoveExercise")

    def exit(self):
        self.controller.refresh_remove_exercise()
        self.controller.show_frame("MainMenu")


class ModifyMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Modify Menu")

        self.change_name_but = tk.Button(self, text="Change Name",
                                         command=lambda: self.controller.show_frame("ChangeName"), width=20, height=3)
        self.change_main_but = tk.Button(self, text="Change Main Muscle",
                                        command=lambda: self.controller.show_frame("ChangeMusclePageOne"),
                                         width=20, height=3)
        self.add_equipment_but = tk.Button(self, text="Add Equipment", command=helloCallBack, width=20, height=3)
        self.remove_equipment_but = tk.Button(self, text="Remove Equipment", command=helloCallBack, width=20, height=3)
        self.change_reference_but = tk.Button(self, text="Change Reference", command=helloCallBack, width=20, height=3)
        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.controller.show_frame("MainMenu"), width=20,
                                  height=3)

        self.change_name_but.pack(pady=5)
        self.change_main_but.pack(pady=5)
        self.add_equipment_but.pack(pady=5)
        self.remove_equipment_but.pack(pady=5)
        self.change_reference_but.pack(pady=5)
        self.exit_but.pack(pady=5)


class ChangeName(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name_error_message = False
        self.exercise_error_message = False

        WAMethods.create_main_label(self, "Change Name")

        WAMethods.pick_an_exercise(self, push_list, pull_list, legs_list, True)

        self.new_name_label = tk.Label(self, text="Enter the new name below")
        self.new_name_label.pack()
        self.new_name_entry = tk.Entry(self)
        self.new_name_entry.pack(pady=10)

        self.exercise_error_label = tk.Label(self, text="Please select an exercise")
        self.name_error_label = tk.Label(self, text="Please enter a name for the exercise before submitting")

        self.next_but = tk.Button(self, text="Sumbit", command=lambda: self.check(), width=20, height=3)
        self.next_but.pack(pady=5)

        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.exit(), width=20,
                                  height=3)
        self.exit_but.pack(pady=5)

    def check(self):
        if not any(self.new_name_entry.get()) and not self.name_error_message:
            self.name_error_label.pack()
            self.name_error_message = True
        if self.exercise_name.get() == "None" and not self.exercise_error_message:
            self.exercise_error_label.pack()
            self.exercise_error_message == True
        if any(self.new_name_entry.get()):
            self.change_name_option()

    def change_name_option(self):
        muscle_group = WAMethods.get_muscle_group(self.group_name.get(), push_list, pull_list, legs_list)

        muscle_group[self.muscle_name.get()][self.new_name_entry.get()] = muscle_group[self.muscle_name.get()].pop(
            self.exercise_name.get())
        master_list[self.new_name_entry.get()] = master_list.pop(self.exercise_name.get())
        master_list[self.new_name_entry.get()].set_name(self.new_name_entry.get())
        self.controller.refresh_all()
        self.controller.show_frame("ChangeName")

    def exit(self):
        self.controller.refresh_change_name()
        self.controller.show_frame("ModifyMenu")

class ChangeMusclePageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.error_message = False

        WAMethods.create_main_label(self, "Change Muscle")

        self.exercise_label = tk.Label(self, text="Select the exercise")
        self.exercise_label.pack()

        WAMethods.pick_an_exercise(self, push_list, pull_list, legs_list, True)

        self.error_label = tk.Label(self, text="Please Select an Exercise Before Submitting")

        self.next_but = tk.Button(self, text="Next", command=lambda: self.check(), width=20, height=3)
        self.next_but.pack(pady=5)

        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.exit(), width=20,
                                  height=3)
        self.exit_but.pack(pady=5)

    def check(self):
        if self.exercise_name.get() == "None" and not self.error_message:
            self.error_label.pack()
            self.error_message = True
        elif self.exercise_name.get() != "None":
            self.controller.show_frame("ChangeMusclePageTwo")

    def exit(self):
        self.controller.refresh_change_muscle()
        self.controller.show_frame("ModifyMenu")

class ChangeMusclePageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Change Muscle")

        self.new_muscle_label = tk.Label(self, text="Select the muscle you want to change the exercise to")
        self.new_muscle_label.pack()

        WAMethods.pick_an_exercise(self, push_list, pull_list, legs_list, False)

        self.next_but = tk.Button(self, text="Submit", command=lambda: self.change_muscle_option(), width=20, height=3)
        self.next_but.pack(pady=5)

        self.exit_but = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("ChangeMusclePageOne"), width=20,
                                  height=3)
        self.exit_but.pack(pady=5)

    def change_muscle_option(self):
        muscle_group = WAMethods.get_muscle_group(self.controller.frames["ChangeMusclePageOne"].group_name.get(),
                                                push_list, pull_list, legs_list)
        muscle_name = self. controller.frames["ChangeMusclePageOne"].muscle_name.get()
        exercise_name = self.controller.frames["ChangeMusclePageOne"].exercise_name.get()

        new_muscle_group = WAMethods.get_muscle_group(self.group_name.get(), push_list, pull_list,legs_list)


        exercise = muscle_group[muscle_name].pop(exercise_name)
        new_muscle_group[self.muscle_name.get()][exercise_name] = exercise
        exercise.set_main(muscle_name)
        self.controller.refresh_all()
        self.controller.show_frame("ChangeMusclePageOne")


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Settings")

        self.add_equipment_but = tk.Button(self, text="Add Equipment",
                                           command=lambda: self.controller.show_frame("AddEquipment")
                                           , width=20, height=3)
        self.remove_equipment_but = tk.Button(self, text="Remove Equipment",
                                            command=lambda: self.controller.show_frame("RemoveEquipment"),
                                              width=20, height=3)
        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.controller.show_frame("MainMenu"),
                                  width=20, height=3)

        self.add_equipment_but.pack(pady=5)
        self.remove_equipment_but.pack(pady=5)
        self.exit_but.pack(pady=5)


class AddEquipment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.error_message = False

        WAMethods.create_main_label(self, "Add Equipment")

        self.text = tk.Text(self, font=font.Font(size=13, weight="bold"), width=50,
                       height=10)
        self.text.insert(tk.INSERT, "Current Equipment\n")
        for i in equipment:
            self.text.insert(tk.INSERT, i+"\n")
        self.text.config(state=tk.DISABLED)
        self.text.pack(pady=5)

        self.equipment_label = tk.Label(self, text="Enter the name of the new Equipment")
        self.equipment_label.pack(pady=5)
        self.equipment_entry = tk.Entry(self)
        self.equipment_entry.pack(pady=5)

        self.error_label = tk.Label(self, text="Please Enter an Equipment Name Before Submitting")

        self.next_but = tk.Button(self, text="Submit", command=lambda: self.check(), width=20, height=3)
        self.next_but.pack(pady=5)

        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.controller.show_frame("Settings"),
                                  width=20, height=3)
        self.exit_but.pack(pady=5)

    def check(self):
        if self.equipment_entry.get() == "" and not self.error_message:
            self.error_label.pack()
            self.error_message = True
        elif self.equipment_entry.get() != "":
            self.add_equipment()


    def add_equipment(self):
        equipment[self.equipment_entry.get()] = self.equipment_entry.get()
        self.controller.refresh_all()
        self.controller.show_frame("AddEquipment")


class RemoveEquipment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Remove Equipment")

        self.text = tk.Text(self, font=font.Font(size=13, weight="bold"), width=50,
                       height=10)
        self.text.insert(tk.INSERT, "Current Equipment\n")
        for i in equipment:
            self.text.insert(tk.INSERT, i + "\n")
        self.text.config(state=tk.DISABLED)
        self.text.pack(pady=5)

        self.equipment_label = tk.Label(self, text="Pick the Equipment to Remove")
        self.equipment_label.pack(pady=5)

        self.equipment_name = tk.StringVar(self)
        if equipment:
            self.equipment_choices = [i for i in equipment]
        else:
            self.equipment_choices = ["None"]
        self.equipment_menu = tk.OptionMenu(self, self.equipment_name, *self.equipment_choices)
        self.equipment_name.set("None")
        self.equipment_menu.pack(pady=5)

        self.next_but = tk.Button(self, text="Submit", command=lambda: self.remove_equipment(), width=20, height=3)
        self.next_but.pack(pady=5)

        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.controller.show_frame("Settings"),
                                  width=20, height=3)
        self.exit_but.pack(pady=5)

    def remove_equipment(self):
        equipment.pop(self.equipment_name.get(), None)
        self.controller.refresh_all()
        self.controller.show_frame("RemoveEquipment")


class Load(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WAMethods.create_main_label(self, "Load")

        self.option1_label = tk.Label(self,
                                      text="Press the button below to keep your current exercises\nand load your save "
                                           "file.")
        self.option1_label.pack()

        self.option1_but = tk.Button(self, text="Option One", command=lambda: self.load_option(False), width=20,
                                     height=3)
        self.option1_but.pack(pady=10)

        self.option2_label = tk.Label(self,
                                      text="Press the button below to erase current exercises\nand load your save file")
        self.option2_label.pack()

        self.option2_but = tk.Button(self, text="Option Two", command=lambda: self.load_option(True), width=20,
                                     height=3)
        self.option2_but.pack(pady=10)

        self.exit_but = tk.Button(self, text="Exit", command=lambda: self.controller.show_frame("MainMenu"), width=20,
                                  height=3)
        self.exit_but.pack(pady=15)

    def load_option(self, option2):
        if option2:
            for muscle in push_list:
                push_list[muscle].clear()
            for muscle in pull_list:
                pull_list[muscle].clear()
            for muscle in legs_list:
                legs_list[muscle].clear()
            master_list.clear()

        file = open("workoutappsave.txt", "r")
        file_save = file.readlines()
        file.close()

        muscle = ""
        exercise = ""
        for line in file_save:
            # Scans for List Type
            if line[0] == "#":
                if line[2:len(line) - 1] == "Push Muscles":
                    muscle_group = push_list
                elif line[2:len(line) - 1] == "Pull Muscles":
                    muscle_group = pull_list
                elif line[2:len(line) - 1] == "Leg Muscles":
                    muscle_group = legs_list
            # Scans for Main Muscle
            elif line[0] == "-":
                muscle = line[2:len(line) - 1]
            # Scans for Exercise Names
            elif line[0] == "+":
                exercise = line[2:len(line) - 1]
                muscle_group[muscle][exercise.lower()] = Exercise(exercise, muscle, [], "")
                master_list[exercise.lower()] = muscle_group[muscle][exercise.lower()]
            # Scans for Equipment
            elif line[0] == "*":
                muscle_group[muscle][exercise.lower()].add_equipment([line[2:len(line) - 1]])
            # Scans for URL Reference
            elif line[0] == "$":
                muscle_group[muscle][exercise.lower()].add_reference([line[2:len(line) - 1]])
            elif line[0] == "/":
                equipment[line[2:len(line)-1]] = line[2:len(line)-1]

        self.controller.refresh_all()
        self.controller.show_frame("ViewExercises")


class Save(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.save_message = False

        WAMethods.create_main_label(self, "Save")

        self.save_but = tk.Button(self, text="Save", command=lambda: self.save_option(), width=20, height=3)
        self.save_but.pack()

        self.exit_but = tk.Button(self, text="Exit", command=self.exit, width=20, height=3)
        self.exit_but.pack(pady=15)

    def save_option(self):
        file = open("workoutappsave.txt", "w+")

        file.write("# Push Muscles")
        for muscle in push_list:
            file.write("\n- " + muscle)
            for exercise in push_list[muscle]:
                file.write("\n+ " + push_list[muscle][exercise].get_name())
                # Statement below ensures the view list doesn't list any empty lists.
                if push_list[muscle][exercise].get_equipment()[0] != "None":
                    for item in push_list[muscle][exercise].get_equipment():
                        file.write("\n* " + item)
                if push_list[muscle][exercise].get_reference()[0] != "None":
                    for reference in push_list[muscle][exercise].get_reference():
                        file.write("\n$ " + reference)

        file.write("\n# Pull Muscles")
        for muscle in pull_list:
            file.write("\n- " + muscle)
            for exercise in pull_list[muscle]:
                file.write("\n+ " + pull_list[muscle][exercise].get_name())
                # Statement below ensures the view list doesn't list any empty lists.
                if pull_list[muscle][exercise].get_equipment()[0] != "None":
                    for item in pull_list[muscle][exercise].get_equipment():
                        file.write("\n* " + item)
                if pull_list[muscle][exercise].get_reference()[0] != "None":
                    for reference in pull_list[muscle][exercise].get_reference():
                        file.write("\n$ " + reference)

        file.write("\n# Leg Muscles")
        for muscle in legs_list:
            file.write("\n- " + muscle)
            for exercise in legs_list[muscle]:
                file.write("\n+ " + legs_list[muscle][exercise].get_name())
                # Statement below ensures the view list doesn't list any empty lists.
                if legs_list[muscle][exercise].get_equipment()[0] != "None":
                    for item in legs_list[muscle][exercise].get_equipment():
                        file.write("\n* " + item)
                if legs_list[muscle][exercise].get_reference()[0] != "None":
                    for reference in legs_list[muscle][exercise].get_reference():
                        file.write("\n$ " + reference)

        for item in equipment:
            file.write("\n/" + item)

        file.close()

        if not self.save_message:
            save_success_label = tk.Label(self, text="Save was successful")
            self.save_message = True
            save_success_label.pack()

    def exit(self):
        self.controller.refresh_save()
        self.controller.show_frame("MainMenu")




class Exercise:

    def __init__(self, name, main, equipment, reference):
        self.name = name
        self.main_group = main
        self.equipment = ["None"]
        if equipment:
            self.equipment = equipment
        self.reference = ["None"]
        if reference:
            self.reference = reference

    def set_name(self, name):
        self.name = name

    def set_main(self, main):
        self.main_group = main

    def add_equipment(self, equip):
        if self.equipment[0] == "None":
            self.equipment = []
        self.equipment.extend(equip)

    def remove_equipment(self, equip):
        self.equipment.remove(equip)
        if not self.equipment:
            self.equipment = ["None"]

    def add_reference(self, reference):
        if self.reference[0] == "None":
            self.reference = []
        self.reference.extend(reference)

    def remove_reference(self, reference):
        self.reference.remove(reference)
        if not self.reference:
            self.reference = ["None"]

    def get_name(self):
        return self.name

    def get_main(self):
        return self.main_group

    def get_equipment(self):
        return self.equipment

    def get_reference(self):
        return self.reference


def helloCallBack():
    messagebox.showinfo("Hello Python", "Feature in progress")


if __name__ == "__main__":
    # Dict to help make searching for exercises faster.
    master_list = {}

    # Dict to help organize exercises and to help AI generate workouts.
    push_list = {"Chest": {}, "Shoulders": {}, "Triceps": {}}
    pull_list = {"Middle Back": {}, "Lower Back": {}, "Lats": {}, "Biceps": {}}
    legs_list = {"Quads": {}, "Hamstrings": {}, "Calves": {}, "Glutes": {}}

    # Dict to hold all equipment
    equipment = {}

    app = AppDriver()
    app.mainloop()