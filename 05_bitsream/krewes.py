#Raymond Lin
#Death Row Coders
#SoftDev
#File Reading
#2024/9/18
#30 min
import random
krewes = open("krewes.txt","r")
person = []
def createList():
    temp = krewes.read().split("@@@")
    for p in temp:
        temp2 = p.split("$$$")
        person.append({"pd":temp2[0], "devo":temp2[1], "ducky": temp2[2]})
createList()
def randomDevo():
    x = random.randint(0,len(person)-1)
    tempDict = person[x]
    return (tempDict["devo"] + " and " + tempDict["ducky"] + " are from pd " + tempDict["pd"] + ".")
print(randomDevo())