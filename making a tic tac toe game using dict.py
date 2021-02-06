# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '} 
 
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# turn = 'X' 
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# printBoard(theBoard)



#guests coming to your house and bringing in the fruits and the quantities of the fruits
allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
    }

def total(guests,item):
    num = 0
    for k,v in allGuests.items():
        num = num + v.get(item,0)
    return str(num)

print("total number of apples are : " + total(allGuests,"apples"))
print("total number of pretzels are : " + total(allGuests,"pretzels"))
print("total number of cups are : " + total(allGuests,"cups"))
print("total number of apple pies are : " + total(allGuests,"apple pies"))
