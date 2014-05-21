#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="beersandrew"
__date__ ="$May 14, 2014 11:42:02 AM$"

if __name__ == "__main__":
    
    # Get test scores
    test1 = float( input( 'Enter the first test score: '))
    test2 = float( input( 'Enter the second test score: '))
    test3 = float( input( 'Enter the third test score: '))
    
    
    # Get average test score
    
    average = ( test1 + test2 + test3 ) / 3.0
    
    # Display the average
    print('The average score is', average )
    