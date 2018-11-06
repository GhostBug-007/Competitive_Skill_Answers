'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here


def inputObject():
    testCases = 0
    seatNum = []
    testCases = int(input())
    while testCases < 1 or testCases > 100000 :
        testCases = int (input())
        
    for seats in range(testCases):
        seatNum.append(int(input()))
        while seatNum[seats] < 1 or seatNum[seats] > 108:
            seatNum[seats]= int (input())
    return (seatNum)                        # Returns a list of the seats
    
def oppositeSeat(seatList , oppSeatList):
    numOfSeats = len (seatList)
    if numOfSeats == 0:
        return oppSeatList
    elif (seatList[0]%12) == 0 :
        seat = ((seatList[0]//12)-1)*12+1
        oppSeatList.append(seat)
        return (oppositeSeat(seatList[1:],oppSeatList))	
    else:
        seat = ((seatList[0] // 12)+1)*12
        seat = seat - (int(seatList[0]%12) -1)
        oppSeatList.append(seat)
        return (oppositeSeat(seatList[1:],oppSeatList))

def seatType(oppSeatList,positionList):
    numOfSeats = len (oppSeatList)
    if numOfSeats == 0:
        return positionList
    else:
        modulo= oppSeatList[0] % 6
        if modulo == 0 or modulo == 1:
            positionList.append("WS")           #Window Seat Condition
        elif modulo%3 == 2 : 
            positionList.append("MS")
        else:
            positionList.append("AS")
        return (seatType(oppSeatList[1:],positionList))


#def main():

seatList = inputObject()               #Function to take the inputs for the program
oppSeatList=[]
positionList=[]
#print(*seatList, sep=" ")
oppositeSeat(seatList,oppSeatList)                 #Function to find the opposite seats
seatType( oppSeatList , positionList )
count= len (positionList)
while count != 0:
    print(str(oppSeatList[0])+" "+str(positionList[0]))
    oppSeatList=oppSeatList[1:]
    positionList=positionList[1:]
    count= len (positionList)    


    



       

            
        
            

