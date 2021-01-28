from datetime import date
import datetime
def covertDateToList():
    today=date.today()
    today_string=today.strftime('%m%d%Y')
    #use find method of string class
    year=today_string.find("2021")
    end=len(today_string)
    start=year
    list= []
    for x in range(start,end):
        list.append(today_string[x])
    return list


def convertListToString(list1):
    new_string = ""
    for i in list1:
         new_string +=i
    return new_string

#year in string
def calculateYear (syear):
    y=int(input("Enter your age: "))
    n=input("Enter your name: ")
    y2=int(input("How many years, you wanna live: "))
    yd=int(syear) + y2
    output="You will probably leave earth on "



    finalOutput=f'{output}{yd}'
    print(finalOutput)


listyear=covertDateToList()
stringyear=convertListToString(listyear)
calculateYear(stringyear)
