
import math

a = 3.6
b = 9
c = 5

print("dataTypes of my coefficients a = {}, b = {},c = {}".format(type(a),type(b), type(c)))

def general_formula(a,b,c):
    determinant = b**2 - 4*a*c

    if (determinant >= 0):
        sol1 = (-b + math.sqrt(determinant))/2*a
        sol2 = (-b - math.sqrt(determinant))/2*a

        print("The equation has two real solution {}, and {} \n".format(sol1,sol2))
    else:
        print("The equation has non real solutiion \n")


# Identify if the equation has a real solution or a complex solution.
if __name__ == "__main__":
    answer_quest = "yes"
    while(answer_quest == "yes"):
        a,b,c = input("Please type the coefficients of your equation: ").split()
        a = float(a)
        b = float(b)
        c = float(c)
        general_formula(a,b,c)

        answer_quest = input("\n Do you want to keep using the application? (yes or no)")