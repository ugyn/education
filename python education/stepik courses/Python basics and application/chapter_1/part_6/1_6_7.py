def updateDaddyList(data):
    try:
        kiddo, daddy = data.split(':')
        daddyList[kiddo.strip()] = daddy.split()
    except:
        daddyList[data.strip()] = []

def isDaddyExist(kiddo):
    if kiddo in daddyList:
        return True
    return False

def getDaddy(big_daddy, kiddo):
    for daddy in daddyList[kiddo]: 
        if big_daddy == daddy:
            return True
    for daddy in daddyList[kiddo]: 
        if getDaddy(big_daddy, daddy) == True:
            return True

daddyList = {}

n = int(input())

for _ in range(n):
    updateDaddyList(input())

q = int(input())

for _ in range(q):
    daddy, kiddo = input().split()
    if isDaddyExist(kiddo) == True:
        if daddy == kiddo:
            print('Yes')
        elif getDaddy(daddy, kiddo) == True:
            print('Yes')
        else:
            print('No')
    else:
        print('No')