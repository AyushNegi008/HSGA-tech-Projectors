import subprocess, sys
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])



import time
import os


print("""
░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗░░░░█████╗░░██████╗
██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║░░░██╔══██╗██╔════╝
██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║░░░██║░░██║╚█████╗░
╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║░░░██║░░██║░╚═══██╗
░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║██╗╚█████╔╝██████╔╝
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░╚════╝░╚═════╝░""")
print("""
[1] continue with setup)
[2] Ive Alredy Done setup
""")
while True:
    setup=input("[?]: ")
    if setup=='1':
        name= input(str("please enter your Username to be Displayed: "))
        pas=input(str("Please enter your password to login: "))

        lines=[name]
        with open('user/username.txt','w')as f:
            f.writelines(lines)
 
        lines4=[pas]
        with open('user/password.txt','w')as f:
            f.writelines(lines4)
        print("setup complete!!!")
        input("press enter to close this And move further to setup: ")

        while True:
            login=input(str("Please Enter The Password To " +name+ ":"))   
            if login==pas:
                open_file("home.py")
                break
            else:
                print("wrong Password")






    elif setup=='2':
        login_pass=open("user/password.txt")
        login_name=open("user/username.txt")
        l_p=login_pass.read()
        l_n=login_name.read()
        while True:
            login=str(input("Please Enter The Password To " +l_n+ ":"))   
            if login==l_p:
                open_file("home.py")
                break
            else:
                print("wrong Password")

    else:
        print("Wrong Input Try Again")
        

        
