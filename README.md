# WHISKY FINDER

#### Video Demo: https://youtu.be/s9gGpoxcy60

#### Description:

This project is a program which finds a scotch whisky distilleries that are most similar to user's taste.

 It works based on database found on kaggle.com. This database originates from site called "Classification of whisky" which unfortunately is no longer accessible. In the program user inputs their favorite scotch distillery and if it is in the database, computer prints out 3 different distilleries which have the highest Sprearman correlation coefficient in relation to the given distillery. 

File "main.py" contains main body of the program, it loads the database, asks user for input, calculates the correlations and outputs the appropriate results. 
File "whisky.csv" contains database of 86 malt whisky distilleries which are scored between 0-4 for 12 different taste categories including sweetness, smoky, nutty etc. 
Source: https://www.kaggle.com/datasets/koki25ando/scotch-whisky-dataset