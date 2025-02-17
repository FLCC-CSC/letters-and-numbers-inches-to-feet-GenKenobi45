# FILE NAME - inches_to_feet.py

# NAME: Yusuf Khan 
# DATE: 02/13/25
# BRIEF DESCRIPTION: Program that oputputs the area of a triangle based on the height and 
# base lengths entered by the user.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




########## ENTER YER CODE BELOW THIS LINE ##########

def find_area():   
    height = float(input('Enter the height: '))
    base = float(input('Enter the base: '))
    area = 0.5*base*height
    print('The area of the triangle is', area)
find_area()

########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?

I feel that the second line of this code kicks off the process becasue it is the first line 
asking for user input, and without that input the program would not be able to output a 
correct answer.

2. What was the hardest part of this lab?

The hardest of the part of this lab was to remeber to use the float funtion to make 
sure the integer can be multiplied by the text.




'''
