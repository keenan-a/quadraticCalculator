import math as m
#split problem
# first we check if there are any solutions to the equation
# x = (-b+/- root delta)/2a,

def main():
    a = int(input("Please provide value for 'a' for your quadratic equation: "))
    b = int(input("Please provide value for 'b' for your quadratic equation: "))
    c = int(input("Please provide value for 'c' for your quadratic equation: "))
    
    delta = m.pow(b,2)-(4*a*c)
    
    if delta < 0:
        print("This is a Complex Number, cannot be solved by my jahash head")
    else:
        root1 = (-b + m.sqrt(delta))/2*a
        root2 = (-b - m.sqrt(delta))/2*a
        print("This is the first quadratic root: " + str(root1))
        print("This is the second quadratic root: " + str(root2))
        print("Bravo ya jahash")

main()