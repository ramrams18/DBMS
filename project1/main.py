transactionlist = {}
locklist = {}
timestamp_counter = 1
class Item(object):
    def __init__(self,name,locktype):
        self.name = name
        self.locktype = locktype
        self.holders = []
        self.waiters = []
        pass
    
class Transaction(object):
    def __init__(self,name,id,state):
        self.name = name
        self.id = id
        self.state = state
        self.lockeditems = []
        self.todoactions = []


def commandparser(cmd):
    cmd = cmd.strip()
    command = cmd[0]
    transaction = cmd[1]
    if command == 'b' or command == 'e':
        item = None
    else:
        cmd = cmd.split("(")
        print(cmd)
        
        item = cmd[1][0]
    return command,transaction,item

def waitdie(transaction , item):
    if locklist[item].locktype == "writelock":
        if transactionlist[locklist[item].holders[0]].id <transactionlist[transaction].id:
            outputfile.write(f"T{transaction} is aborted due to wait-die\n")
            abort(transaction)
            return False
        else:
            
            
            
            
            transactionlist[transaction].state = "waiting"
            
            outputfile.write(f"T{transaction} is blocked/waiting due to wait-die.\n")
            return True
    if locklist[item].locktype == "readlock":
        if len(locklist[item].holders)>1:
            pass
        for i in locklist[item].holders:
            if transactionlist[i].id <transactionlist[transaction].id:
                outputfile.write(f"T{transaction} is aborted due to wait-die\n")
                
                abort(transaction)
                return False
            else:
                pass

        transactionlist[transaction].state = "waiting"
        outputfile.write(f"T{transaction} is blocked/waiting due to wait-die.\n")
        
        return True

def begin(transaction):
    global timestamp_counter
    transactionlist[transaction] = Transaction(transaction,timestamp_counter,"active")
    outputfile.write(f"T{transaction} begins. Id={timestamp_counter}. TS={timestamp_counter}. state=active.\n")

    timestamp_counter+=1

def read(transaction , item):
    if transaction in transactionlist and transactionlist[transaction].state == "waiting":
        outputfile.write(f"reading T{transaction} is added to operation list.\n")
        transactionlist[transaction].todoactions.append(f"r{transaction} ({item})")
        return
    if transactionlist[transaction].state == "blocked":
        transactionlist[transaction].todoactions.append(i)
    else:
        if item not in locklist:
            locklist[item] = Item(item,"unlock")
        readlock(transaction , item)
   
def write(transaction , item):
    if transaction in transactionlist and transactionlist[transaction].state == "waiting":
        outputfile.write(f"writing T{transaction} is added to operation list.\n")
        transactionlist[transaction].todoactions.append(f"w{transaction} ({item})")
        return
    if item not in locklist:

        locklist[item] = Item(item,"unlock")
    writelock(transaction , item)
      
def end(transaction):
    if transaction in transactionlist and transactionlist[transaction].state == "waiting":
        outputfile.write(f"committing T{transaction} is added to operation list.\n")
        transactionlist[transaction].todoactions.append(f"e{transaction}")
        return
    commit(transaction)
    
def commit(transaction):
    while (len(transactionlist[transaction].lockeditems)>0):
        item = transactionlist[transaction].lockeditems.pop(0)
        unlock(transaction,item)
    
    transactionlist[transaction].state = "commited"
    outputfile.write(f"T{transaction} is committed\n")

def unlock(transaction, item):

    item = locklist[item]
    if item.locktype == "unlock":
        return
    elif item.locktype == "readlock":
        if len(item.holders) >1:

            item.holders.remove(transaction)


        elif len(item.holders) == 1 :

            item.holders.remove(transaction)
            item.locktype = "unlock"
            

            if len(item.waiters)>0:

                resume(item.waiters[0])

                
    elif item.locktype == "writelock":

        item.holders.remove(transaction)
        item.locktype = "unlock"


        if len(item.waiters)>0:

            resume(item.waiters[0])
def resume(transaction):
    if transactionlist[transaction].state == "aborted":
        return
    else:
        transactionlist[transaction].state == "active"
    for action in transactionlist[transaction].todoactions:
        if transaction.state == "waiting" or "aborted" or "commited":
            return
        else: compute(action)    
        
def abort(transaction):
    transactionlist[transaction].state = "aborted"
    if len(transactionlist[transaction].lockeditems) >0:
        for item in transactionlist[transaction].lockeditems:
            unlock(transaction,item) 
             
def readlock(transaction , item):

    if locklist[item].locktype == 'unlock' or locklist[item].locktype == 'readlock':
        locklist[item].locktype = 'readlock'
        transactionlist[transaction].lockeditems.append(item)
        locklist[item].holders.append(transaction)
        outputfile.write(f"{item} is read locked by T{transaction}\n")
    elif locklist[item].locktype == 'writelock':
        waitdie(transaction ,item)
    pass
        
def writelock(transaction , item):

    if locklist[item].locktype == 'unlock':
        locklist[item].locktype = "writelock"
        transactionlist[transaction].lockeditems.append(item)
        outputfile.write(f"{item} is write locked by T{transaction}\n")
        

        
        
    elif len(locklist[item].holders) == 1 and locklist[item].holders[0] == transaction:
        locklist[item].locktype = "writelock"
        outputfile.write(f"read lock on {item} by T{transaction} is upgraded to write lock\n")

    else:

        waitdie(transaction,item)
        
        
        
def compute(cmd):
    outputfile.write(cmd.strip(" \n")+" ")

    command , transaction, item = commandparser(cmd)

    if transaction in transactionlist and transactionlist[transaction].state == "aborted":
        outputfile.write(f"T{transaction} is already aborted.\n")
        return
    
    if command == 'b':
        begin(transaction)
    elif command == "r":
        read(transaction,item)
    elif command == "w":
        write(transaction,item)
    elif command == "e":
        end(transaction)

outputfile = open("output.txt","w")
file = open("input.txt",'r')
for i in file:
    compute(i)
            
            