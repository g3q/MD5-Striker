import md5
from datetime import datetime
import time
from time import sleep

print ("  __  __   ___    ___     ___   _____   ___   ___   _  __  ___   ___  ")
print (" |  \/  | |   \  | __|   / __| |_   _| | _ \ |_ _| | |/ / | __| | _ \ ")
print (" | |\/| | | |) | |__ \   \__ \   | |   |   /  | |  | ' <  | _|  |   / ")
print (" |_|  |_| |___/  |___/   |___/   |_|   |_|_\ |___| |_|\_\ |___| |_|_\ ")
print ("                                                        Created by loctang ")

print ("             ")
print (" MD5 Striker is made to crack MD5 Hashes and find the plain text in the corsponding text file ")
print (" ANY ILLEGAL ACTIVITY IS NOT MY FAULT, THIS IS MADE FOR PENETRATION TESTERS, NOT CRIMINALS! ")

                                                                     
                                                                                                          

now = datetime.now()
the_hour = now.hour
the_min = now.minute
the_sec = now.second

counter = 1

pass_in = raw_input("\nEnter the MD5 Hash: ")
pwfile = raw_input("\nEnter the File Name: ")

try:
    pwfile = open(pwfile, "r")
except:
    print("\nERROR: Could Not Find The Entered File; Please Try Again!")
    quit()

for password in pwfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    print("Cracking Password %d: %s") % (counter, password.strip())

    counter += 1

    if pass_in == filemd5:
        print("\nThe Hash Has Been Cracked! \nThe Password is: %s") % password

        now2 = datetime.now()
        the_hour2 = now2.hour
        the_min2 = now2.minute
        the_sec2 = now2.second

        print('\nCrack Started at ' + str(the_hour) + ":" + str(the_min) + "." + str(the_sec))
        print('Crack Ended at ' + str(the_hour2) + ":" + str(the_min2) + "." + str(the_sec2) + "\n")
        print("Thank You For Using MD5 Striker!")
        break

else:
    now2 = datetime.now()
    the_hour2 = now2.hour
    the_min2 = now2.minute
    the_sec2 = now2.second

    print("\nPassword Not Found, Try A Stronger, Bigger Password List.")

    print('\nStarted at ' + str(the_hour) + ":" + str(the_min) + "." + str(the_sec))
    print('Ended at ' + str(the_hour2) + ":" + str(the_min2) + "." + str(the_sec2) + "\n")
