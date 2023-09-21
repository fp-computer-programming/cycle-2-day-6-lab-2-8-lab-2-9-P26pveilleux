""""
Create a Python file named lab_2-8.py
A team needs to score 15 points to win a gold medal, between 12-14 points to win a silver medal, 
and between 9-11 point to win a bronze medal. A team does not earn a medal if they earn 8 or fewer points.
Write a program using nested if else statements where a user can input the number of points a team scored and the medal that they earned is displayed.
"""""
x = 15

if x >= 15:
    print ("gold medal.")
if x >12:
    print ("you are in silver.")
elif x > 14:
    print ("you are out of silver.")
if x > 9:
    print ("you are in bronze.")
elif x < 9:
    print ("you are out of bronze")
if x < 8: 
    print ( "you failed.")


