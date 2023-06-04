import os,platform

os.system('git pull')

 

Ahmer=platform.architecture()[0]

if Ahmer=="32bit":

    print('Sorry 32 Bit Not Supported...')

elif Ahmer=="64bit":

    #print('Command is in update wait we will fix it soon !')

    __import__("Ahmer")
