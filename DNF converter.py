key = ["<>",">>","~","&","|"]   

from sympy.abc import *
from sympy.logic import simplify_logic
import re

def checkHowManyLogicOperations(expression):
    numberOfOperations = {"&":0,"~":0,">>":0,"<>":0,"|":0}
    for i in key:
        occurences = expression.count(i)    #Count how many times each logic operation is in the expression
        numberOfOperations[i] = occurences

    return numberOfOperations

#Remove Bi-Implications (<>):
def removeBiImp(statement):
    (left,right) = statement.split('<>',1)  #Split from first occurence of <>
    statement = "("+left+">>"+right+") & ("+right+">>"+left+")"
    return statement

#Remove Implications (>>):
def removeImp(statement):
    (left,right) = statement.split('>>',1)  #Split from first occurence of >>
    statement = "~"+left+"|"+right
    return statement

#Move Negation (~):
def moveNeg(statement):
    list = re.findall('\(([^)]+)', statement)  #List of all sub-brackets
    for i in range(len(list)):
        if "~~" in statement:
            statement = statement.replace("~~","")
            print("Double Negations cancel:")
            print(statement)

        if "~("+list[i]+")" in statement:
            statement = statement.replace("~("+list[i]+")",  str(simplify_logic("~("+list[i]+")"))    ) #I.e. ~(z) === ~z
            print("Open brackets:")
            print(statement)

        #If it's just ~A then leave it

    return statement

def check(expression,numberOfLogicOperations):  
    #List all sub-brackets
    old = expression
    list = re.findall('\(([^)]+)', expression)  #List of all sub-brackets
    #print(list)
    
    for i in range(len(list)):
        if ("<>" in list[i]): #Check if <> is in statement
            expression = expression.replace(list[i],removeBiImp(list[i]))  #Replaces all <> within sub-prackets appropriately
            print("Remove Bi-Implications:")
            print(expression)
            numberOfLogicOperations = checkHowManyLogicOperations(expression) #RE-CALCULATE as new symbols may have formed

        if (">>" in list[i]): #Check if >> is in statement
            expression = expression.replace(list[i],removeImp(list[i]))  #Replaces all <> within sub-prackets appropriately
            print("Remove Implications:")
            print(expression)
            numberOfLogicOperations = checkHowManyLogicOperations(expression)

    #Replaces all <> outside of sub-prackets 
    numberOfBiImp = numberOfLogicOperations["<>"]
    while numberOfBiImp>0:
        expression = removeBiImp(expression)
        print("Remove Bi-Implications:")
        print(expression)
        numberOfLogicOperations = checkHowManyLogicOperations(expression)
        numberOfBiImp = numberOfLogicOperations["<>"]

    #Replaces all >> outside of sub-prackets 
    numberOfImp = numberOfLogicOperations[">>"]
    while numberOfImp>0:
        expression = removeImp(expression)
        print("Remove Implications:")
        print(expression)
        numberOfLogicOperations = checkHowManyLogicOperations(expression)
        numberOfImp = numberOfLogicOperations[">>"]

    #Check no more symbols are in the expression
    while (numberOfLogicOperations[">>"]>0) or (numberOfLogicOperations["<>"]>0):
        expression = check(expression,numberOfLogicOperations)
        
    expression = moveNeg(expression)    #Move negatives

    print("Tidy Up / Move disjunctions outwards:") #i.e.( remove redundant parenthesis if needed) & (Move disjunctions outwards if needed)
    expression = simplify_logic(eval(expression))
    print(expression)
        
    return expression


#Ensure ONLY NECCESARY BRACKETS ARE ENTERED (i.e."(A&B)" != "A&B")
expression = "~(A>>B)"
#print("Simplified:",simplify_logic(expression,'dnf')) - QUICKLY FIND THE END SOLUTION IF NEEDED
numberOfLogicOperations = checkHowManyLogicOperations(expression)
print()
print("Start:",expression)
value = check(expression,numberOfLogicOperations)


