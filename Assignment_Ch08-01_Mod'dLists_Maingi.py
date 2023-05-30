#
# # Samuel Maingi
# # Assignment 08-01
# # 04/024/2023


def createList(listSize):
    timeList = [0] * listSize
    return timeList

def fillList(listSize, timeList):
    for i in range(listSize):
        timeList[i] = i

hoursList = createList(24)
fillList(24, hoursList)
minutesList = createList(60)
fillList(60, minutesList)

daysList = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
responseList = ['y', 'n']

def collectUserInputTime():
    while True:
        try:
            userTime = input("Enter the time the call started in 24-hour notation (hh:mm):\n ")
            startHour, startMinute = userTime.split(":")
            startHour = int(startHour)
            startMinute = int(startMinute)
            if startHour not in hoursList or startMinute not in minutesList:
                raise ValueError
            return str(startHour), str(startMinute)
        except ValueError:
            print("\nInvalid time input.\nPlease try again.\n")

def validateUserInputTime(startHour, startMinute):
    startHour = int(startHour)
    startMinute = int(startMinute)
    if startHour < 0 or startHour > 23:
        return False, None, None
    if startMinute < 0 or startMinute > 59:
        return False, None, None
    return True, startHour, startMinute

def collectUserInputDay():
    while True:
        try:
            userDay = input("\nEnter the day the call started (Mo, Tu, We, Th, Fr, Sa, Su):\n ")
            firstDayCharacter = userDay[0].lower()
            secondDayCharacter = userDay[1].lower()
            if firstDayCharacter+secondDayCharacter not in daysList:
                raise ValueError
            return firstDayCharacter, secondDayCharacter
        except ValueError:
            print("\nInvalid day input.\nPlease try again.\n")

def validateUserInputDay(firstDayCharacter, secondDayCharacter):
    if firstDayCharacter+secondDayCharacter in daysList:
        return True
    else:
        return False

def collectUserInputCallLength():
    while True:
        callLength = input("\nEnter the length of the call in (hours:minutes):\n ")
        try:
            callLengthHour, callLengthMinute = map(int, callLength.split(':'))
            if callLengthHour >= 0 and callLengthMinute >= 0 and callLengthMinute < 60:
                return callLengthHour, callLengthMinute
            else:
                print("\nInvalid length of call input.\nPlease try again.\n")
        except ValueError:
            print("\nInvalid length of call input.\nPlease try again.")

def validateUserInputCallLength(callLengthHour, callLengthMinute):
    if int(callLengthHour) >= 0 and int(callLengthMinute) >= 0:
        return True
    else:
        return False

def calculateTotalCost(startHour, startMinute, firstDayCharacter, secondDayCharacter, callLengthHour, callLengthMinute):
    startHour = int(startHour)
    startMinute = int(startMinute)
    callLengthHour = int(callLengthHour)
    callLengthMinute = int(callLengthMinute)
    if firstDayCharacter+secondDayCharacter in ['sa', 'su']:
        costPerMinute = 0.15
    elif startHour < 8 or (startHour == 18 and startMinute != 0) or startHour > 18:
        costPerMinute = 0.25
    else:
        costPerMinute = 0.4
    totalCost = (callLengthHour * 60 + callLengthMinute) * costPerMinute
    return totalCost

def collectUserInputYesNo():
    response = input("\nDo you want to repeat the program (y/n)?:\n ")
    return response.lower()

def validateUserInputYesNo(response):
    if response.lower() not in ['y', 'n']:
        return False
    return True

def main():
    hoursList = createList(24)
    fillList(24, hoursList)
    minutesList = createList(60)
    fillList(60, minutesList)

    startHour, startMinute = collectUserInputTime()
    while not validateUserInputTime(startHour, startMinute):
        print("Invalid input. Please try again.\n")
        startHour, startMinute = collectUserInputTime()

    firstDayCharacter, secondDayCharacter = collectUserInputDay()
    while not validateUserInputDay(firstDayCharacter, secondDayCharacter):
        print("Invalid input. Please try again.\n")
        firstDayCharacter, secondDayCharacter = collectUserInputDay()

    callLengthHour, callLengthMinute = collectUserInputCallLength()
    while not validateUserInputCallLength(callLengthHour, callLengthMinute):
        print("Invalid input. Please try again.\n")
        callLengthHour, callLengthMinute = collectUserInputCallLength()

    totalCost = calculateTotalCost(startHour, startMinute, firstDayCharacter, secondDayCharacter, callLengthHour, callLengthMinute)
    print("The cost of the call is: $%.2f" % totalCost)

    YesOrNo = collectUserInputYesNo()
    while not validateUserInputYesNo(YesOrNo):
        print("Invalid input. Please try again.\n")
        YesOrNo = collectUserInputYesNo()

    if YesOrNo.lower() == 'y':
        main()

if __name__ == '__main__':
    main()