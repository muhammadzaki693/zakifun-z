import termcolor
import time
from termcolor import colored

def create():
  print("created")

def template(select):
  if select == "hello world":
    print("hello world")
  elif select == "calculator":
    while 1:
      x = int(input("type a number: "))
      z = int(input("type an number: "))
      y = input("select: ")
      
      if y == "+":
        print(x+z)
      elif y == "-":
        print(x-z)
      elif y == "×":
        print(x*z)
      elif y == "^":
        print(x**z)
      else:
        print(colored("uknown: "+y, "red"))
        break
  elif select == "python terminal":
    while 1:
      x2 = input(">>> ")
      if x2 == "exit":
        print("restart")
        time.sleep(3)
        print("done")
        break
      
      try:
        y2 = eval(x2)
        print(y2)
      except:
        try:
          exec(x2)
        except Exception as e:
          print("error: ",e)
  elif select == "custom":
    while 1:
      r = input("execute: ")
      
      try:
        exec(r)
      except Exception as e:
        print("error uknown to exec another error: ",e)
  elif select == "open":
    while 1:
      j = input("file to open and read: ")
      file = open(j, "r")
    
      print(file.read())
  else:
    print(colored("selectError: undefine", "red"))

def command(commands):
  if commands == "-V" or commands == "--version":
    print("1.1.0")
  elif commands == "__name__":
    print(__name__)