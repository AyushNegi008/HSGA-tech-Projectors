'''
file=open('com.txt',"w")
file.write("Now the file has more content!")
file.close()



#1
file=input('Enter the file: ') 
f =open( file,'r') 
item=[] 
for line in f: 
    words=line.split() 
for i in words: 
    item.append(i) 
print('#'.join(item)) 





#2
def cnt():
    f=open("com.txt","r")
    cont=f.read()
    print(cnt)
    v=0
    cons=0
    l_c_l=0
    u_c_l=0
    for ch in cont:
        if (ch.islower()):
            l_c_l+=1
        elif(ch.isupper()):
            u_c_l+=1
        ch=ch.lower()
        if( ch in ['a','e','i','o','u']):
            v+=1
        elif (ch in ['b','c','d','f','g',
                     'h','j','k','l','m',
                     'n','p','q','r','s',
                     't','v','w','x','y','z']):
            cons+=1
    f.close()
    print("Vowels are : ",v)
    print("consonants are : ",cons)
    print("Lower case letters are : ",l_c_l)
    print("Upper case letters are : ",u_c_l)      
#main program
cnt()




#3

file=open('hp.txt',"r")
lines=file.readline()
file.close()

file=open('hp.txt',"w")
file2=open('hp2.txt',"w")
for line in lines:
    if 'a' in line:
        file2.write(line)
    else:
        file.write(line)
file.close()
file2.close()

file=open('hp.txt',"r")
file2=open('hp2.txt',"r")
b=file.readlines()
c=file2.readlines()
print(b)
print(c)
file.close()
file2.close()




#4
import pickle
import sys
dict={}
def write_in_file():
    file=open("stud2.txt","ab")  #a-append,b-binary
    no=int(input("ENTER NO OF STUDENTS: "))
    for i in range(no):
        print("Enter details of student ", i+1)
        dict["roll"]=int(input("Enter roll number: "))
        dict["name"]=input("enter the name: ")
        pickle.dump(dict,file)  #dump-to write in student file
    file.close()
 
def display():
    #read from file and display
    file=open("stud2.txt","rb")   #r-read,b-binary
    try:
        while True:
            stud=pickle.load(file)   #write to the file
            print(stud)
    except EOFError:
        pass
    file.close()
 
def search():
    file=open("stud2.txt","rb")   #r-read,b-binary
    r=int(input("enter the rollno to search: "))
    found=0
    try:
        while True:
            data=pickle.load(file)   #read from file
            if data["roll"]==r:
                print("The rollno =",r," record found")
                print(data)
                found=1
                break
    except EOFError:
        pass
    if found==0:
        print("The rollno =",r," record is not found")
    file.close()
 
#main program


while True:       
    print("MENU \n 1-Write in a file \n 2-display ")
    print(" 3-search\n 4-exit \n")
    ch=int(input("Enter your choice = "))
    if ch==1:
        write_in_file()
    if ch==2:
        display()
    if ch==3:
        search()
    if ch==4:
        print(" Thank you ")
        sys.exit()



#5
import pickle
rollno=int(input('Enter roll number:'))
name=input('Enter Name:')
marks=int(input('Enter Marks'))

def insertRec():
    rollno=int(input('Enter roll number:'))
    name=input('Enter Name:')
    marks=int(input('Enter Marks'))

rec={'Rollno':rollno,'Name':name,'Marks':marks}
f=open('stt.txt','ab')
pickle.dump(rec,f)
f.close()
'''


#6
a=input("enter to roll a dice")
def random():
    import random
    s=random.randint(1,6)
    return s
print(random()) 


#7
answer = input("Do you have an account?(yes or no) ")
if answer == 'yes' :
   login = False
   csvfile = open("Username password.csv","r")
   reader = csv.reader('Username password.csv')
   username = input("Player One Username: ")
   password = input("Player One Password: ")
   for row in reader:
        if row[0]== username and row[1] == password:
           login = True
        else:
           login = False
   if login == False:
      print("Incorrect. Game Over.")
      exit()
   else:
      print("You are now logged in!")
else:
   print('Only Valid Usernames can play. Game Over.')
   exit()





import _____________             # Line 1
def addCsvFile(UserName,PassWord):     # to write / add data into the CSV file  f=open(' user.csv','________')                 # Line 2 newFileWriter = csv.writer(f)  newFileWriter.writerow([UserName,PassWord])  f.close()  #csv file reading code  def readCsvFile():               # to read data from CSV file  with open(' user.csv','r') as newFile:  newFileReader = csv._________(newFile)            # Line 3  for row in newFileReader:  print (row[0],row[1])  newFile.______________                                    # Line 4  addCsvFile(“Arjun”,”123@456”)  addCsvFile(“Arunima”,”aru@nima”)  addCsvFile(“Frieda”,”myname@FRD”)  readCsvFile() #Line 5 Read more on Sarthaks.com - https://www.sarthaks.com/968882/ranjan-kumar-class-writing-program-create-which-will-contain-name-password-some-entries
