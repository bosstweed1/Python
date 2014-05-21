#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="beersandrew"
__date__ ="$May 19, 2014 9:49:22 AM$"


# Global variables 

# Variables for Activity 2
budgetvars = {"hourlyRate":20.0, "overtimeRate":30.0,
            "regularHours":40.0, "overtimeHours":10.0, 
            "rentAmount":600, "percentEle":.05, "percentWater":.01, 
            "percentSewer":.02, "percentGas":.10, "foodBudget":300, "entertainment":250,
            "carBudget":400}
'''
hourlyRate = 20
overtimeRate = 30
regularHours = 40
overtimeHours = 10
rent = 600
percentEle = .05
precentWater = .01
percentSewer = .02
percentGas = .10
foodBudget = 300
entertainment = 250
carBudget = 400
'''

# **activity_one**
# Input: None
# Output: Text
# Description: A customized welcome message within the command console
#              including your name and description of your program.
    
def activity_three():
    return raw_input('Please enter your name: ')
    
    
# **activity_two**
# Input: (global) variables
# Output: Text
# Description: A print out of the variables of the program, their values, and types
#              
    
def activity_two():
    print("Here is a dump of all the variables, their values, and their data types:\n")
    
    print("Variable Name\t : Value\t : Type\n")
    for key in budgetvars:
        print key, "\t : ", budgetvars[key], "\t : ", type(budgetvars[key])
        
    '''
    print("old")
    print("hourlyRate : %d : %s" % (hourlyRate, type(hourlyRate) ) )
    print("hourlyRate : %s : %s" % (budgetvars["hourlyRate"], type(budgetvars["hourlyRate"]) ) )
    print("overtimeRate : %d : %s" % (overtimeRate, type(overtimeRate) ) )
    print("regularHoursWorked : %d : %s" % (regularHoursWorked, type(regularHoursWorked) ) )
    print("overtimeHoursWorked : %d : %s" % (overtimeHoursWorked, type(overtimeHoursWorked) ) )
    print("rent : %d : %s" % (rent, type(rent) ) )
    print("percentElectricBill : %.2f : %s" % (percentElectricBill, type(percentElectricBill) ) )
    print("precentWaterBill : %.2f : %s" % (precentWaterBill, type(precentWaterBill) ) )
    print("percentSewerBill : %.2f : %s" % (percentSewerBill, type(percentSewerBill) ) )
    print("percentGasBill : %.2f : %s" % (percentGasBill, type(percentGasBill) ) )
    print("foodBudget : %d : %s" % (foodBudget, type(foodBudget) ) )
    print("entertainmentBudget : %d : %s" % (entertainmentBudget, type(entertainmentBudget) ) )
    print("carBudget : %d : %s" % (carBudget, type(carBudget) ) )
    '''

# **activity_three**
# Input: None
# Output: Text
# Description: A customized welcome message within the command console
#              including your name and description of your program.
    
def activity_one( user ):
    print ("\nWelcome, %s." % user)
    print ("Description: This is a budget calculator program.")
    print ("Author: Andrew Beers\n\n")

    
if __name__ == "__main__":
    
    # Function for Activity 3
    username = activity_three()
    
    # Function for Activity 1
    activity_one( username )
    
    # Function for Activity 2
    activity_two()