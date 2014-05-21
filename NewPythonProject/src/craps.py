# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import random
import math
__author__="beersandrew"
__date__ ="$May 13, 2014 9:20:26 AM$"

if __name__ == "__main__":
    
    payTable = [0, 0, 30, 15, 1.8, 1.4, 1.1666666, 4, 1.1666666, 1.4, 1.8, 15, 30 ]
    point = 0 # this means that its the come out roll
    bet = 5
    payout = 0
    
    # mode = int( raw_input("Manual mode (type rolls) -1 Automatic mode ( random rolls) -0: "))
    mode = 1
    # Main game loop
    while( True ):
        # Dice roll
        if ( mode ):
            roll = raw_input("Enter the roll (i.e. 8) ( q to quit ): ")
            #die1 = int(roll[0])
            #die2 = int(roll[1])
        else:
            die1 = math.ceil( random.random() * 6)
            die2 = math.ceil( random.random() * 6)
            roll = die1 + die2;
            
        if ( roll == 'q'):
            break;
        
        bet = raw_input("Enter the bet (i.e. 5): ")
        
        # Check for hards
        #hard = ( die1 == die2 )
        sum = int(roll)
        
        #print ( "The roll was %s %s : %s" % (die1, die2, sum) )
        
        
        # See if we 
        #if ( point == 0 and sum > 3 and sum < 11 ): # Set the point
        #    point = sum
        #elif ( point != 0 and sum == 7 ): # Lose
        #    point = 0
        #elif ( point != 0 and sum == point ): # Front line win
        #    point = 0
            
            
        print ( "Results: ")
    
        print ( "%s pays %s " % ( sum, payTable[sum] * float(bet) ) )
