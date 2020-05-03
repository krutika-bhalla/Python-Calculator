import re
print ("Our Magical Calculator")
print("Type 'quit' to exit")
prev=0
run = True
def performMath():
    global run
    global prev
    equa = ""
    if prev == 0:
        equa = input("Enter Equation: ")
    else:
        equa = input(str(prev))
    
    
    if equa == 'quit':
        print("Goodbye Human :)")
        run = False
    else:
        equa = re.sub('[a-zA-z,.:()" "]','',equa)


        if prev == 0:
            prev = eval(equa)
        else:
            prev = eval(str(prev) + equa)
        


while run==True:
    performMath()