# from main import userchoice1
# from main import endprogram
def waitscreen(seed):
  global userchoice0
  exitornot=input("\n$$  >> Press 1 to continue  <<   $$\n$$  >> Press 0 to exit      <<   $$\n >> ")
  if(exitornot=='1'):
    print("\n\n*************************************************************")
    userchoice0=1
  else:
    print('*************************************************************\n ')
    userchoice0=0
  return userchoice0
 