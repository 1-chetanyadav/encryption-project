import json
import os
import datetime

from encrypt import seed
time = datetime.datetime.now()
def mmixer(message):


# Define the file path
# file_path = "F:/aa/vscode/hotval/tkinter/data.txt"

 writer= open("data.txt",'a')
 writer.write("\nMessage: "+ str(message)+"   Seed: "+str(seed) + "  Time: "+str(time))
 writer.close()
  
def base64saver(message2):
 writer= open("data.txt",'a')
 writer.write("\nMessage: "+ str(message2)+"  No Seed " + "  Time: "+str(time))
 writer.close()

