import subprocess, sys
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
import time
import os
import socket
import psutil

battery = psutil.sensors_battery()
login_pass=open('user/password.txt')
login_name=open('user/username.txt')
l_p=login_pass.read()
l_n=login_name.read()
print("""
░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗░░░░█████╗░░██████╗
██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║░░░██╔══██╗██╔════╝
██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║░░░██║░░██║╚█████╗░
╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║░░░██║░░██║░╚═══██╗
░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║██╗╚█████╔╝██████╔╝
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░╚════╝░╚═════╝░
""")
print("welcome " +l_n)
print("The Date Is:" + time.strftime("%m/%d/%y"))
print("the battery level is:",battery.percent)
print(""""
[1] To open google
[2] To open text editor
[3] To open file explorer
[4] To configure and open Bios
[5] To close os safley
""")
while True:
    select=input("[?]: ")
    if select=='1':
        open_file("brows.py")

    elif select=='2':
        open_file('edit.py')

    elif select=='3':
        open_file('file.py')

    elif select == '4':
        while True:
            b_login=input(str("Please Enter The Password To " +l_n + " To Open Bios: "))
            if b_login== l_p:
                print("Opening Bios")
                host_name = socket.gethostname()
                host_ip = socket.gethostbyname(host_name)
                print("[1] User NAME: " +l_n)
                print("[2] PASSWORD: " +l_p)
                print("Hostname:",host_name)
                print("LOCAL IPS:" +host_ip)
                edit_b=input("Enter 1 to change name \n Enter 2 to change password: ")
                if edit_b=='1':
                    edit_n=input("Enter New Username: ")
                    with open("user/username.txt","w")as f:
                        f.writelines(edit_n)
                    print("User Name Changed To" +edit_n)
                    input("Press Enter To Close Window: ")
                
                if edit_b=='2':
                    edit_p=input("Enter New Password: ")
                    with open("user/password.txt","w")as f:
                        f.writelines(edit_p)

                    print("Password Changed To" +edit_p)
                    input("Press Enter To Close Window: ")
            else:
                print("Wrong Password to " +l_n)

    elif select=='5':
        print("Shuting Down")
        break         
    else:
        print("Wrong Input Try Again")            
