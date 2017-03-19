"""
This program reads in data from stdin and then checks to see what operators are
needed between "+" and "*" to get a provided total. If it is possible it will
return a string representing the formula to use, or if not it will return
"impossible".

Oliver Reid - 2569385
"""

#Imports
from sys import stdin
import itertools

#Globals
values = []
target = False
mode = False

##
# This method takes the mode, values and sucessful operators and gives an
# answer detailing the mode, values and operators that worked.
#
# @param mode The mode determing how to calculate the total.
# @param values The values that totalled to the target.
# @param group The operators, in order, which were used to get the target.
# @return A string representing the answer.
##
def giveAnswer(mode, values, group):
    answer = mode
    for index, val in enumerate(values):
        if index == len(group):
            answer += " " + str(val)
        else:
            answer += " " + str(val) + " " + str(group[index])
    return(answer)

##
# This method reads the data read in from stdin, from the global variable and
# finds the formula that gets the supplied target, using the supplied mode.
#
# @return The formula string.
##
def calculate():
    #Declare our variables
    operators = list(itertools.product(['+', '*'], repeat=(len(values) - 1)))
    
    #Check for easy base case
    if len(values) == 1:
        if values[0] == target:
            return(mode + " " + str(values[0]))
        else:
            return(mode + " impossible")
    
    #Do the rest
    for group in operators:
        added = 0
        multiplied = 0
        if mode == 'L':
            total = values[0]
            i = 0
            for index, val in enumerate(values):
                if index == 0:
                    continue
                if index == len(group):
                    if group[index - 1] == '+':
                        total += val
                    elif group[index - 1] == '*':
                        total *= val
                else:
                    if group[i] == '+':
                        total += val
                    elif group[i] == '*':
                        total *= val
                    i += 1
            #Check to see if we have the correct formula
            if(total == target):
                return(giveAnswer(mode, values, group))
        elif mode == 'N':
            for index, val in enumerate(values):
                if index == 0:
                    if group[index] == '+':
                        added = val
                    if group[index] == '*':
                        multiplied = values[index] * values[index + 1]
                elif index == len(group):
                    if group[index - 1] == '+':
                        added += val
                else:
                    if group[index] == '+' and group[index - 1] == '+':
                        added += val
                    elif group[index] == '*':
                        if group[index - 1] == '+':
                            multiplied += values[index] * values[index + 1]
                        elif group[index - 1] == '*':
                            multiplied *= values[index + 1]
            #Check to see if we have the correct formula
            if((added + multiplied) == target):
                return(giveAnswer(mode, values, group))
    
    #We didn't find the correct answer
    return(mode + " impossible")

##
# Main routine
##
for userinput in stdin:    
    #Check if the input is blank
    if not userinput.strip():
        continue

    #Check to see if we can ast it
    try:
        #Remove spaces for casting
        input = userinput.replace(" ", "")
        input = input.replace("-", "")
        
        #Cast to see if we throw an exception
        value = int(input)
    except ValueError:
        target = int(userinput.split(' ')[0])
        mode = userinput.strip('\n').split(' ')[1]

        print(calculate())
    else:
        values = map(int, userinput.split())
        