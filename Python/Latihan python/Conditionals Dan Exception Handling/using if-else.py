try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 4.0 >= your_GPA >= 3.80:
            print(f"Damn you've got a magna cumlaude with your {your_GPA}GPA")
        elif 3.50 <= your_GPA < 3.80:
            print(f"Cool!! You've got a cumlaude with your {your_GPA} GPA")
        elif 3.00 <= your_GPA < 3.50:
            print(f"You've got a stable GPA tho")
        elif your_GPA < 3.0:
            print(f"You need a stable GPA")
    else:
        print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except ValueError:
    print("Please enter a valid GPA")
