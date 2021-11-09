
def calculate_gp(grade, cl):
    grade = input("Enter your Grade: ").upper()
    cl = int(input("Enter the credit unit: "))
    cgp = 0
    if grade == 'A':
        cgp = 5 * cl
    elif grade == 'B':
        cgp = 4 * cl
    elif grade == 'C':
        cgp = 3 * cl
    elif grade == 'D':
        cgp = 2 * cl
    elif grade == 'E':
        cgp = 1 * cl
    elif grade == 'F':
        cgp = 0
    else:
        print("invalid grade, please contact the IT unit")
    print(f"Your GP is {cgp}")


calculate_gp('A', 3)

