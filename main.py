#  import_________________________
result = 25

#  def____________________________

def greet():
    #  greeting & hint of answer, x ** 2 = 6(example)
    print("Start!!")
    print("What number is this?")
    print("Result is", result)

def hint(i):
    """
    this method is like hint.
    first,player enter the number that player think.
    second,the number change a type to "int".
    third,calculate
    finally,display calculation result.
    if the number is not number,error message display but program do not finish.
    """
    localResult = None
    print(i)
    tenAnswer = input("Please enter the number that you think. ")
    #  print(type(tenAnswer))
    try:
        intTenAnswer = int(tenAnswer)
        localResult = intTenAnswer**2 
        print(localResult)
    except ValueError:
       print("that is not number") 


def reply():
    rep = input("What do you reply? ")
    try:
        intRep = int(rep)
        if intRep ** 2 == result:
            print("correct!!")
        else:
            print("incorrect...")
    except ValueError:
        print("that is not number")


#  main_______________________



greet()

for elem in [1,2,3]:
    hint(elem)

reply()

input("Press Enter...")
