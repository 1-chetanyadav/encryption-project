from encrypt import seed
from encrypt import mixer
from decrypt import dixer
from saver import mmixer
from history import loadhis
from enbase64 import mybaseisu
from enbase64de import mybaseisud
from result import waitscreen
# seed

userchoice0 ='1'
# print(userchoice0)
#main menu
while (userchoice0 !=0):
  userchoice1=input("*************************************************************\n\n###  Welcome to Encryption and Decryption program  ###\n\n1.To Encrypt       2.To Decrypt\n3.History          4.About Program\n>> ")

  if userchoice1=="1":
    userchoice2=input("\n1. Personal Encryption or 2. Base64 Encryption \n>> ")
    if userchoice2=='1':
       message=input("\nType your message: ")
       mixed=mixer(message)
       print("\nEncrypted Text:",mixed)
       # print(seed)
       mixedd=mmixer(mixed)
       # print(mixedd)
       print("Seed: ",seed)
      #  print("\nuserchoice0== ",userchoice0)
       userchoice0=waitscreen(userchoice0)
      #  print("\nuserchoice0== ", userchoice0)
    #   print(userchoice0)
    elif userchoice2=='2':
       message2=input("\nType your message: ")
       mybaseisu(message2)
       userchoice0=waitscreen(userchoice0)
    else:
        print("\nInvalid Input !! \n")
       
  
  elif userchoice1=="2":
    userchoice3=input("\n1. Personal Encryption or 2. Base64 Encryption\n>> ")
    if userchoice3=='1':
       enmessage=input("Message to decrypt: ")
       enseed=input("Type seed: ")
       undixer=dixer(enmessage)
       userchoice0=waitscreen(userchoice0)
       # print(undixer)
    elif userchoice3=='2':
       message2d=input("\nMessage to decrypt: ")
       mybaseisud(message2d)
       userchoice0=waitscreen(userchoice0)
    else:
        print("\nInvalid Input !! \n")

  elif userchoice1=="3":
    loadhis()
     # with open("data.json") as r:
     #     data=json.load(r)
     #     print("\ndata\n")
    
  elif userchoice1=="4":
     print("This program provide 2 types of\n message encryption and decryption\n\n1. Custom Encryption\n2. Base64\n\nYOU CAN CHANGE CUSTOM ENCRYTION ACCORDING TO YOUR NEED")
     userchoice0=waitscreen(userchoice0)
#  elif userchoice0=='0':
#    print(" Thanks for using our program ;) ")
       

  else:
     print("Invalid Input Found!")

print(" Thanks for using our program ;) \n")
