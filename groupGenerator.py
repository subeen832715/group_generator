print("Please enter the total number of students.")
studentNumber = int(input())
 
print("Please enter the number of groups")
numGroups = int(input())

 
def createNamelist(num):
 print("Please enter the names of the students.")
 nameList = []
 for x in range(num):
    print("Student", x+1, "first name: ")
    firstname = input()
    print("Student", x+1, "last name: ")
    lastname = input()
    fullname = lastname + ' ' + firstname
    nameList.append(fullname)
 return nameList
 
 
 
def alphabetSort(list):
 list.sort()
 return list
 
 
import random
 
def randomSort(list):
 random.shuffle(list)
 return list
 
 
def grouping(num, arr):
    teamNumber = []
    for x in range(numGroups):
        teamNumber.append(x+1)
    teamNumber.reverse()

    groupDict = {}
    for x in range(numGroups):
        groupDict[x+1] = []

    for x in range(numGroups):
        teamList=[]
        groupSize = round(num/teamNumber[x])
        for y in range(groupSize):
            teamList.append(arr[0])
            arr.pop(0)
        groupDict[x+1] = teamList
        num -= groupSize
    print(groupDict)
    return(groupDict)


def search(groupDict):
    searchName = input("Enter the name of the student: ")
    for group, name in groupDict.items():
        for x in name:
            if x == searchName:
                print(searchName, "belongs to group", group)



 
 
presort = createNamelist(studentNumber)
# sortedList = randomSort(presort)
sortedList = alphabetSort(presort)
group = grouping(studentNumber, sortedList)
search(group)

