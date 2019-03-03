from datetime import datetime

now = datetime.now()
f_today = open("last_log.txt", "r")
x = (f_today.read())

print "Log file for today-"
print x

f_log = open("log.txt", "a")
f_log.write(str(now)+"\n")
f_log.write(x)
f_log.write("\n")