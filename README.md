# DBMS Models and Implementation techniques

# Project 1: 

Description:

1. Readlock(): This method will first query all records in the lock list for a specific item. If no
record is found, it will insert an entry into the lock list indicating that the transaction has locked the item and will also update the transaction list. Otherwise, it will check to see if the item is locked by a non-conflicting transaction or if it is unlocked, and then it will update the lock and transaction lists accordingly. Otherwise, the item is write locked by another transaction, and wait_die is called to determine what action to take.

2. Writelock(): This method will search the lock list for a specific item. If the item is read locked by the same transaction, the lock will be upgraded to a write lock. If the item is already unlocked, it will simply lock it by updating the record in the lock list. If it is write locked by another transaction, it will call wait_die to determine what action to take. If more than one transaction is reading an item and another transaction is requesting a conflicting lock, apply wait_die to all of the pairs of transactions and if all of the results are wait, the transaction will wait; otherwise, if any of the results is abort, the transaction will abort.

3. Unlock(): This method will unlock the item for the transaction by updating the item's state to unlock, and it will grant the lock to any waiting transactions for this item. It will also execute the waiting operations for the transactions that have been granted lock from the transaction list and change the transaction's status to active.

4. Wait_die(): Using the timestamp stored in the transaction list, this method will determine which transactions will wait and which will abort during the deadlock.

5. Abort(): This method will unlock all locks for the specific transaction and update the transaction list's status if the transaction was aborted.

6. Commit(): This method simply unlocks all transaction locks and updates the transaction list's status to committed for the specific transaction.
 
Code Execution:

* This code was tested with python version 3.9.13
	
* Run the main.py and input.txt file in the same folder to get the required output.

Please Enter the command line argument as mentioned below:

         python3 main.py <inputfile> 

Example:
  
         python3 main.py input.txt 

* Generated output3.txt file is in input3 folder

# Project 2: 

-> How to run?

* Make sure That dnspython, urllib, json and pymongo dependencies are installed in the environment that you are evaluating

* Initialization.ipynb contains the code that is required for populating sql and mongoldb databases

* main.ipynb contains code for evaluating the mongodb find operations for the database.

-> Steps to execute main.ipynb

1. Open the main.ipynb in any (preferred Jupyter ) notebook and execute the cells sequentially to get the output. ADD any find queries in the last cells if you want to get more results

2. Here we have used a cloud mongodb resource for easy querying without any setup.

3. If you want to run every thing on local system then open the initialization file and run all cells sequentially and make sure to change the MongoDB client to local as mentioned in the notebook comments. And run the main.ipynb sequentially by changing client to local to get output.

Packages to install :   

                     pip install dnspython
                     
                     pip install ‘pymongo[srv]’
                        
Programming Language Used : Python3

Compiler: Jupyter Notebook                         
