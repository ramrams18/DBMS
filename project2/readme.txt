
Programming Language Used : Python3

Compiler: Jupyter Notebook 

->how to run?

-Make sure That dnspython, urllib, json and pymongo dependencies are installed in the environment that you are evaluating

-Initialization.ipynb contains the code that is required for populating sql and mongoldb databases

-main.ipynb contains code for evaluating the mongodb find operations for the database.

->Steps to execute main.ipynb

1. open the main.ipynb in any (preferred Jupyter ) notebook and execute the cells sequentially to get the output. ADD any find queries in the last cells if you want to get more results

2. Here we have used a cloud mongodb resource for easy querying without any setup.

3. If you want to run every thing on local system then open the initialization file and run all cells sequentially and make sure to change the MongoDB client to local as mentioned in the notebook comments. And run the main.ipynb sequentially by changing client to local to get output.