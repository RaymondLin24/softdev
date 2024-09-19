#Raymond Lin
#Louie-Lin 4 Da Win
#SoftDev
#Reading a CSV File
#2024/9/19
#

import random
import csv

with open('occupations.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in spamreader: