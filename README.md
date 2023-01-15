# Share-from-Py2-to-Py3-
This is a Windows example of how to create a Pandas DataFrame in Python 2 and then store it using REDIS so that you can read it into a Python 3 code.... REDIS is running in Ubuntu under the WSL2 layer in Windows. Python 2 and Python 3 are running in separate shells under windows (using miniconda). Not a production ready solution, just a way to make things work in this scenario. 

To get Ubuntu running under WSL on Windows:

https://medium.com/data-engineering-on-cloud/setup-ubuntu-20-04-using-wsl-on-windows-11-61a6451aab65

For REDIS, use these links:

https://github.com/redis/redis-om-python

https://redis.io/docs/getting-started/installation/install-redis-on-windows/

to get things installed and running in Ubuntu under Windows. 
Start the REDIS server in Ubuntu at the command line:

>sudo service redis-server start


STEP 1: 

Run the python 2 code:
 
> python io_test_py2.py
 
(in a PY2 miniconda shell for example).

STEP 2:
 
Then in Ubuntu under Windows wsl2 at the command line:

> redis-cli
 
 (starts the REDIS CL interface)
 
 This is just so you can see what is passing thorugh there and not necessary. 
 
>  ping
 
 (you should get a pong)
 
> get 'ch5'
 
 (you should get the return item for that key that was saved)
 
 > get 'ch7'
  
 (should see the pandas data frame in a somewhat garbled text CSV format but that's ok- we deal with it later in the reader)
 
STEP 3:
  
From a Python 3 shell (in miniconda for example), run the Python 3 code:
  
> python io_test_py3.py

