# Sort namelist in alphabetical order
def alphabetSort(list):
 list.sort()
 return list
 
# Random-sort namelist
import random
 
def randomSort(list):
 random.shuffle(list)
 return list

# Grouping function
# def grouping(num, method):
#     if sortMethod == "Alphabetical order":
#         arr = alphabetSort(nameList)
#     elif sortMethod == "Random":
#         arr = randomSort(nameList)

#     teamNumber = []
#     for x in range(numGroups):
#         teamNumber.append(x+1)
#     teamNumber.reverse()

#     groupDict = {}
#     for x in range(numGroups):
#         groupDict[x+1] = []

#     for x in range(numGroups):
#         teamList=[]
#         groupSize = round(num/teamNumber[x])
#         for y in range(groupSize):
#             teamList.append(arr[0])
#             arr.pop(0)
#         groupDict[x+1] = teamList
#         num -= groupSize
#     lbl_output.value = groupDict

# # Search function
# def search(groupDict, fullname):
#     for group, name in groupDict.items():
#         for x in name:
#             if x == fullname:
#                 lbl_output.value = fullname + "belongs to group" + group



from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox

app = App(title="Group Generator")
welcomeMessage = Text(app, text="Welcome to Group Generator!")

# Pass user input (1. number of students/ 2. number of groups) from the textbox into grouping function
# 1. Number of students
studentNumber_label = Text(app, text="Total number of students")
studentNumberStr = TextBox(app, text= "Please enter a number")

try:
    studentNumber = int(studentNumberStr.value)
except ValueError:
    print('invalid input')

# 2. Number of groups
groupNumber_label = Text(app, text="Number of groups")
numGroupsStr = TextBox(app, text = "Please enter a number")

try:
    numGroups = int(numGroupsStr.value)
except ValueError:
    print('invalid input')

studentNumber = 10
message3 = Text(app, text="Students' names")
nameList = []
for x in range(studentNumber):
    if x < studentNumber/2:
        firstnameMessage = Text(app, text="First name", align="left")
        firstname = TextBox(app)
        lastnameMessage = Text(app, text="Last name", align="left")
        lastname = TextBox(app)
        btn_add = PushButton(app, text='Add', align="left")
        btn_add.bg="gray"
    else:
        firstnameMessage = Text(app, text="First name", align="right")
        firstname = TextBox(app)
        lastnameMessage = Text(app, text="Last name", align="right")
        lastname = TextBox(app)
        btn_add = PushButton(app, text='Add', align="right")
        btn_add.bg="gray"

    fullname = lastname.value + ' ' + firstname.value
    nameList.append(fullname)
    print(nameList)


# message4 = Text(app, text="Select grouping method:")
# sortMethod = ButtonGroup(app, options=["Alphabetical order", "Random"], selected="Alphabetical order")

# btn_group = PushButton(app, text='Go!', command=grouping(studentNumber, sortMethod))
# lbl_output = Text(app, text="Grouping result")
# groupDict = lbl_output.value
# btn_group.bg="gray"


# findNameMessage = Text(app, text="Student's name")
# firstnameFind = TextBox(app)
# lastnameFind = TextBox(app)
# fullnameFind = lastnameFind + ' ' + firstnameFind

# btn_search = PushButton(app, text='Go!', command=search(groupDict, fullnameFind))
# lbl_output = Text(app, text="Grouping result")
# btn_search.bg="gray"




app.display()