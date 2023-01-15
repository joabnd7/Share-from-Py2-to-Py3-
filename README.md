# Share-from-Py2-to-Py3-

Major frustration in dealing with Py2 and Py3 code that has to run in realtime together while sharing data. I know to veterans this is probably the obvious solution, but it was kind of tricky, so to save others some pain, I decided to post a solution. This is a Windows example of how to create a Pandas DataFrame in Python 2 and then store it using REDIS so that you can read it into a Python 3 code. The reason for this is a company X who has not created Py3 drivers for their hardware Y or Z. In order to use the hardware, you are stuck with Py2, but in reality, for GUIs and UX, you would like to be using Py3... REDIS is running in Ubuntu under the WSL2 layer in Windows.

To get Ubuntu running under WSL on Windows:
https://medium.com/data-engineering-on-cloud/setup-ubuntu-20-04-using-wsl-on-windows-11-61a6451aab65

For REDIS, use these links:

https://github.com/redis/redis-om-python

https://redis.io/docs/getting-started/installation/install-redis-on-windows/

to get things installed and running in Ubuntu under Windows. 
Start the REDIs server with:
in Ubuntu at the command line:
 <Ubunutu> sudo service redis-server start


STEP 1: 

Run the python code:
 
<py2> python io_test_py2.py
 
(in a PY2 miniconda shell for example).


STEP 2:
 
Then in Ubuntu under Windows wsl2 at the command line:

<Ubunutu> redis-cli
 
 (starts the REDIS CL interface)
 
 This is just so you can see what is passing thorugh there and not necessary. 
 
<Ubunutu>  ping
 
 (you should get a pong)
 
<Ubunutu> get 'ch5'
 
 (you should get the return item for that key that was saved)
 
 <Ubunutu> get 'ch7'
  
 (you should get your pandas data frame in a somewhat garbled text CSV format but that's ok- we deal with it later in the reader)
 
STEP 3:
  
From a Python 3 shell (in miniconda for example)
  
<py3> python io_test_py3.py

