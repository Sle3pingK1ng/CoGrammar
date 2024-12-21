timeswimmming = ("time event complete in minius")
timecycling = ("time event complete in minius")
timerunning = ("time event complete in minius")
totaltime = sum(timeswimmming + timecycling + timerunning)
print(totaltime)

if (totaltime > 100) or (totaltime <101):
    print("Honorary colours")
elif (totaltime >101) or (totaltime <105):
    print("Honorary half colours")
elif (totaltime >105) or (totaltime >110):
    print("Honorary scroll")
elif (totaltime >110):
    print("Sorry no award")

