from ast import Num
import DB_Handler
#How to use
#DB_Handler.CallDB(List)
#This takes a list of commands

# Starting Values
# These are the values the system requires to run pulled from DB
Users = []

# Generated values


# These values are generated by functions 
Cards = []

Quizes = []

# functions
def RetrieveUser(user):
    user_info = DB_Handler.SearchDB("users", "username", user)
    for i in user_info:
        print(i)
        return(i)

def login(name):
    user = RetrieveUser(name)
    if user is None:
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        DB_Handler.InsertIntoDB("users", (name, password))
        #this default card keeps the queries that run from passing nothing later on
        DB_Handler.InsertIntoDB("cards", (1, user, "user", "users", user))
        startup()
    password = input("Enter your password: ")
    if password == user[1]:
        return(user)
    else:
        print("Wrong password try again")
        startup()

def DisplayQuizzes():
    Display = ""
    Quiznum = 0 
    for i in Cards:
        if i[3] not in Quizes:
            Quizes.append(i[3])
            if i[3] != "users":
                Display = Display + " " + i[3] + "[" + str(Quiznum) + "]"
    print(Display)
    num = input("type the number of the quiz you would like to select ")
    return (Quizes[int(num)])


def RetrieveQuiz(quiz):
    for i in Cards:
        if i[3] == quiz:
            print(i[1])
            print(i[2])
            print("")

def startup():
    name = input("Eneter your username: ")
    #login is disabled for testing purposes
    #login(name)
    DBCards = DB_Handler.SearchDB("cards", "user", name)
    for i in DBCards:
        Cards.append(i)
    RetrieveQuiz(DisplayQuizzes())



#main
startup()