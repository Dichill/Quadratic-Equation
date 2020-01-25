#
#
#   Made by Dichill/DrX
#   Github.com/Dichill
#
#
#

# Import >>
import os
import math
import cmath

# Colors >>
g = '\033[1;32m' # green
r = '\033[1;31m' # red
nc = '\033[0m'  #no color

# Clear >>
os.system("cls")

# Variables >>
MultipliedResults = 0
DividedResults = 0
AddedResults = 0
SubtractedResults = 0
ExponentResults = 0

# Check if Solution is Correct >>
Solution_1 = False
Solution_2 = False

a = 0
b = 0
c = 0
Signs1 = 0
Signs2 = 0

# Load >>
def Load():
   
   # Calculations
    def Multiplication(x, y):
        MultipliedResults = x * y
    def Division(x, y):
        DividedResults = x / y
    def Addition(x, y):
        AddedResults = x + y
    def Subtraction(x, y):
        SubtractedResults = x - y
    def Exponent(x):
        ExponentResults = x ** 2
    
    # Questioning
    print(r + "DrX Quadratic Equation Solver")
    print("Usually Quadratic Equations has form of ax^2 + bx + c = 0 ")
    print("So we use the Quadratic Formula to Solve an Equation.")
    
    Operation = input(g + "Solve for Roots(r) | Quit(q): ")
    if Operation == "R" or Operation == "r":
        a = float(input(nc + "Enter A: "))
        b = float(input(nc + "Enter B: "))
        c = float(input(nc + "Enter C: "))

        d = (b**2) - (4*a*c)

        if d >= 0:
            sol1 = (-b-cmath.sqrt(d))/(2*a)
            sol2 = (-b+cmath.sqrt(d))/(2*a)
        else:
            x_1 = complex((-b/(2*a)),math.sqrt(-d)/(2*a))
            x_2 = complex((-b/(2*a)),-math.sqrt(-d)/(2*a))

        if d < 0:
            print (r + "This equation has no real solution")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            print ((g + "This equation has one solutions: "), round(x, 3))
            #add the extra () above or it does not show the answer just the text

            Check = input("Do you want to Check the equation? Y/n: ")
            if Check == "Y" or Check == "y" or Check == "Yes" or Check == "yes":
                x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
            x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
            final = round(x1, 3)
            print (g + "This equation has two solutions: ", x1, " or", x2)
            Check = input("Do you want to Check the equation? Y/n: ")
            if Check == "Y" or Check == "y" or Check == "Yes" or Check == "yes":
                ch1_exp = x1 ** 2
                ch1_1 = a * ch1_exp
                ch1_2 = b * x1
      
                print(r + "===========================================================")
                print("Checking the Quadratic Equation with different Signs #1 SOLUTION")
                print("===========================================================")
                print("Checking #1 : {0}x^2 + {1}x + {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 + ", abs(b), " * ", abs(x1), " + ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " + ", round(abs(ch1_2), 3), " + ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) + round(abs(c), 3))
                calculation_1 = round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) + round(abs(c), 3)    
                if calculation_1 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution1_1 = True;
                    
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print("===========================================================")
                print("Checking #2 : {0}x^2 - {1}x - {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 - ", abs(b), " * ", abs(x1), " - ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " - ", round(abs(ch1_2), 3), " - ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) - round(abs(c), 3))
                calculation_2 = round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) - round(abs(c), 3)    
                if calculation_2 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution1_1 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print("===========================================================")
                print("Checking #3 : {0}x^2 - {1}x + {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 - ", abs(b), " * ", abs(x1), " + ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " - ", round(abs(ch1_2), 3), " + ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) + round(abs(c), 3))
                calculation_3 = round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) + round(abs(c), 3)    
                if calculation_3 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution1_1 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print(r +"===========================================================")
                print("Checking #4 : {0}x^2 + {1}x - {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 + ", abs(b), " * ", abs(x1), " - ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " + ", round(abs(ch1_2), 3), " - ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) - round(abs(c), 3))
                calculation_4 = round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) - round(abs(c), 3)    
                if calculation_4 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution1_1 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                
        else:
            x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
            x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
            print (g + "This equation has two solutions: ", x1, " or", x2)
            Check = input("Do you want to Check the equation? Y/n: ")
            if Check == "Y" or Check == "y" or Check == "Yes" or Check == "yes":
                ch1_exp = x1 ** 2
                ch1_1 = a * ch1_exp
                ch1_2 = b * x1
      
                print(r + "===========================================================")
                print("Checking the Quadratic Equation with different Signs #1 SOLUTION")
                print("===========================================================")
                print("Checking #1 : {0}x^2 + {1}x + {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 + ", abs(b), " * ", abs(x1), " + ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " + ", round(abs(ch1_2), 3), " + ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) + round(abs(c), 3))
                calculation_1 = round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) + round(abs(c), 3)    
                if calculation_1 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_1 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print("===========================================================")
                print("Checking #2 : {0}x^2 - {1}x - {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 - ", abs(b), " * ", abs(x1), " - ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " - ", round(abs(ch1_2), 3), " - ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) - round(abs(c), 3))
                calculation_2 = round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) - round(abs(c), 3)    
                if calculation_2 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_1 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print("===========================================================")
                print("Checking #3 : {0}x^2 - {1}x + {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 - ", abs(b), " * ", abs(x1), " + ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " - ", round(abs(ch1_2), 3), " + ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) + round(abs(c), 3))
                calculation_3 = round(abs(a), 3) * round(abs(ch1_exp), 3) - round(abs(ch1_2), 3) + round(abs(c), 3)    
                if calculation_3 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_1 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print(r +"===========================================================")
                print("Checking #4 : {0}x^2 + {1}x - {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x1), "^2 + ", abs(b), " * ", abs(x1), " - ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3), " + ", round(abs(ch1_2), 3), " - ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) - round(abs(c), 3))
                calculation_4 = round(abs(a), 3) * round(abs(ch1_exp), 3) + round(abs(ch1_2), 3) - round(abs(c), 3)    
                if calculation_4 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_1 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")

                # Nevermind These
                print("")
                print("")

                ch2_exp = x2 ** 2
                ch2_1 = a * ch2_exp
                ch2_2 = b * x2
                
                print(r + "===========================================================")
                print("Checking the Quadratic Equation with different Signs #2 SOLUTION")
                print("===========================================================")
                print("Checking #1 : {0}x^2 + {1}x + {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x2), "^2 + ", abs(b), " * ", abs(x2), " + ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3), " + ", round(abs(ch2_2), 3), " + ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3) + round(abs(ch2_2), 3) + round(abs(c), 3))
                calculation_1 = round(abs(a), 3) * round(abs(ch2_exp), 3) + round(abs(ch2_2), 3) + round(abs(c), 3)    
                if calculation_1 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_2 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print(r + "===========================================================")
                print("Checking #2 : {0}x^2 - {1}x - {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x2), "^2 - ", abs(b), " * ", abs(x2), " - ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3), " - ", round(abs(ch2_2), 3), " - ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3) - round(abs(ch2_2), 3) - round(abs(c), 3))
                calculation_2 = round(abs(a), 3) * round(abs(ch2_exp), 3) - round(abs(ch2_2), 3) - round(abs(c), 3)    
                if calculation_2 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_2 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print(r)
                print(r + "===========================================================")
                print("Checking #3 : {0}x^2 - {1}x + {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x2), "^2 - ", abs(b), " * ", abs(x2), " + ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3), " - ", round(abs(ch2_2), 3), " + ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3) - round(abs(ch2_2), 3) + round(abs(c), 3))
                calculation_3 = round(abs(a), 3) * round(abs(ch2_exp), 3) - round(abs(ch2_2), 3) + round(abs(c), 3)    
                if calculation_3 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_2 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print(r +"===========================================================")
                print("Checking #4 : {0}x^2 + {1}x - {2}".format(a, b, c))
                print("= ",abs(a), " * ", abs(x2), "^2 + ", abs(b), " * ", abs(x2), " - ", abs(c))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3), " + ", round(abs(ch2_2), 3), " - ", round(abs(c), 3))
                print("= ", round(abs(a), 3) * round(abs(ch2_exp), 3) + round(abs(ch2_2), 3) - round(abs(c), 3))
                calculation_4 = round(abs(a), 3) * round(abs(ch2_exp), 3) + round(abs(ch2_2), 3) - round(abs(c), 3)    
                if calculation_4 == 0:
                    print(g + "Correct Solution! Checking IS Equal to 0!")
                    Solution_2 = True;
                else:
                    print(r + "Wrong Solution! Checking is not equal to 0!")
                print("=================================================")

                print(g + "=================================================")
                print(g + "Conclusion")
                print(g + "=================================================")
                
                if Solution_1 == True:
                    print(g + "In Conclusion {0} is the Answer!".format(x1))
                elif Solution1_1 == True:
                    print(g + "In Conclusion {0} is the Answer!".format(x1))                
                else:
                    print(r + "Checking ERROR | Either theres no answer or the Solution is wrong!")

                if Solution_2 == True:
                    print(g + "In Conclusion {0} is the Answer!".format(x2))
               #except :
                #   print("Cannot Check. Try to manually solve it by rounding it off to the nearest hundreth.")
                            
        #print(g + "=================================================")
        #print(g + "Conclusion")
        #print(g + "=================================================")
        #print(r + "0j is not part of the Solution!")
        #print(g + 'Solution: {0} and {1}'.format(sol1, sol2))
        #print(g + "=================================================")            

    elif Operation == "Q" or Operation == "q":
        os.system("quit")
    else:
        print(r + "Incorrect Format!")
Load();
