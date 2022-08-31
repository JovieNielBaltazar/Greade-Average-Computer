print("welcome to average computer!")
num_of_subjects = int(input("how many subjects do you have?: "))
grades = []
proceed_to_method = ""

def make_list():
    x = 0
    while x < num_of_subjects:
        grade = int(input("enter grade here: "))
        grades.append(grade)
        x += 1

def average():
    total = sum(grades)
    average_of_grades = total / len(grades)
    print(average_of_grades, "is your average!!")

def ask_to_proceed():
    proceed_to_method = input("are these your correct grades? If not, type no to enter grades again: ")

    if proceed_to_method.lower() == "yes":
        average()
    else:
        make_list()
        ask_to_proceed()
        if proceed_to_method.lower() == "yes":
            average()

make_list()

print("these are your grades:", grades)
ask_to_proceed()



