import os
file = open('time.txt' , 'r')
time = file.read()

#def reboot():
    #os.system(f"reboot -r {time}")

#reboot()
print(time)