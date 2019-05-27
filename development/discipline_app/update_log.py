from datetime import datetime
import os

# now = datetime.now()
now = "hello"
project_folder = os.environ['TEMP']
print project_folder

f_today = open(project_folder + "/last_log.txt", "r")
x = (f_today.read())

print "Log file for today-"
print x

f_log = open("$TEMP/log.txt", "a")
f_log.write(str(now)+"\n")
f_log.write(x)
f_log.write("\n")