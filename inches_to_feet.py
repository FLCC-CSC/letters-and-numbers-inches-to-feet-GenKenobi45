# FILE NAME - inches_to_feet.py

# NAME: Yusuf Khan
# DATE: 02/14/25
# BRIEF DESCRIPTION: program converts inches entered by user to feet.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





# BEWARE! You'll need to cast not only the input from the user
# but also maybe the number of feet

########## ENTER YER CODE BELOW THIS LINE ##########
    
def convert():
    inches = int(input('Enter the number of inches: '))
    feet = int(inches / 12)
    remainder = inches % 12
    print(inches, 'inches is', feet, 'feet, and', remainder, 'inches')
convert()    
    
    
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the number of inches: 14

14 inches is 1 feet, and 2 inches


'''



'''

Enter the number of inches: 100

100 inches is 8 feet, and 4 inches

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does it mean to "cast" input from the user?

to cast input from the user means to convert the input from the user to another data type 
from the original string of data.




'''
