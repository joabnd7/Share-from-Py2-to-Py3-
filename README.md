# Share-from-Py2-to-Py3-

Major frustration in dealing with Py2 and Py3 code that has to run in realtime together. I know to veterans this is the obvious solution, but it was kind of tricky, so to save others weeks of pain, I decided to post a solution. This is a Windows example of how to create a Pandas DataFrame in Python 2 and then store it using REDIS so that you can read it into a Python 3 code. The reason for this is a company X who has not created Py3 drivers for their hardware. In order to use the hardware, you are stuck with Py2, but in reality, for GUIs and UX, you would like to be using Py3... REDIS is running in Ubuntu under WSL2 in Windows. 
https://medium.com/data-engineering-on-cloud/setup-ubuntu-20-04-using-wsl-on-windows-11-61a6451aab65

Use these links:

https://github.com/redis/redis-om-python

https://redis.io/docs/getting-started/installation/install-redis-on-windows/

to get things installed in Ubuntu under Windows. 

Run the python code 
https://github.com/joabnd7/Share-from-Py2-to-Py3-/blob/main/io_test_py2.py
in PY2 miniconda shell.

Then in Ubuntu under Windows wsl2 at the command line:

 redis-cli
 (starts the REDIS CL interface)
 
 then type: 
 
 ping
 (you should get a pong)
 
 get 'ch5'
 (you should get shit)
 
 get 'ch7'
 (you should get your pandas data frame in a somehwat garbled text CSV format but that's ok)
 
 your Python3 code can get this....don't believe me .... try it :)
 
 https://github.com/joabnd7/Share-from-Py2-to-Py3-/blob/main/io_test_py3.py
 
 
 
