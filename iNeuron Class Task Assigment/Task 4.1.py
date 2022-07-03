'KISHOR DEVARAGUDI'
# Write a code to get time in your system
import datetime
present = datetime.datetime.now()
print ("Current Time : ")
print (present.strftime("%H:%M:%S"))

# write a code to fatch date from your system
import datetime
now = datetime.datetime.now()
print ("Current Date  : ")
print (now.strftime("%Y-%m-%d"))

# write a code to send mail to your friend
import smtplib

gmail_user = 'kishordev36gmail.com'
gmail_password = 'Kishordevu46'

sent_from = gmail_user
to = ['kishordevu46@gmail.com']
subject = 'Python Mail'
body = 'This is sent using Python'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

# alarm scheduled time
# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x200")


# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time=f"({hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")

            # Wait for one seconds
            time.sleep(1)

            # Get current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time, set_alarm_time)

            # Check whether set alarm is equal to current time or not
            if current_time == set_alarm_time:
                print("Time to Wake up")
                # Playing sound
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
                 )
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()

# write a code to check IP address of your system
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

# write a code to check perticular installation in your system
# importing the module
import subprocess

# traverse the software list
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(Data)

# try block
try:

    # arrange the string
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[6:][i])

except IndexError as e:
    print("All Done")


# string to convert integer:
def length_str(string):
    counter = 0
    if type(string) != str:
        print("Please enter a string")
    else:
        for s in string:
            counter += 1
            string += s
    return counter


length_str('ABCDEFGHIJKHdsadsank')

# premitive
def get_index(l):
  for i in range(0,len(l)):
    print(i,':',l[i])

get_index([1,2,3,4,5])
get_index([1,16,17,[1,2,3,4,5]])

# which will take a dict and gives a list
# Approch 1

def dict_to_list(d):
    list1 = []
    for key, val in d.items():
        list1.append([key, val])
    return list1


print(dict_to_list({"Name": "kishor", "Qualification": "BE", "YOE": 2}))

#Approach 2

def dict_to_list2(d):
  list2 = []
  for i in d:
    k = [i, d[i]]
    list2.append(k)
  return list2

print(dict_to_list2({"Name":"Gaurav", "Qualification":"MBA","YOE":2}))

# multiple list as input and gives concatination of it as output
def list_concat(list1, list2, list3):
    for x in list2:
        list1.append(x)

    for x in list3:
        list1.append(x)

    return list1


print(list_concat(["x", "y", "z"], [1, 2, 3], ['kishor', 'ineuron', 109]))

# list of all file
import os


def all_files(path):
    list = []
    for (root, dirs, file) in os.walk(path):
        for f in file:
            list.append(f)
    return list


# Function Call
print(all_files("D:\pycham Project\kishor"))

# to fillter out one word file
def filter_word_files(directory):
  for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(('.doc', '.docx')):
            print(filename)

filter_word_files("D:\pycham Project\kishor")

#Answer 25 (Function to access Mail)



