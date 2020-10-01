import sys
# import os
# os.system("") ???

reset = "\u001b[0m"

bold =      "\33[1m"
italic =    "\33[3m"
url =       "\33[4m"
blink =     "\33[5m"
underline = "\u001b[4m"
reversed =  "\u001b[7m"

class fg():
   black =     "\u001b[38;5;0m"
   gray =      "\u001b[38;5;8m"
   red =       "\u001b[38;5;9m"
   green =     "\u001b[38;5;10m"
   yellow =    "\u001b[38;5;11m"
   blue =      "\u001b[38;5;12m"
   purple =    "\u001b[38;5;13m"
   cyan =      "\u001b[38;5;14m"
   white =     "\u001b[38;5;15m"
class bg():
   black =  "\u001b[48;5;0m"
   gray =   "\u001b[48;5;8m"
   red =    "\u001b[48;5;9m"
   green =  "\u001b[48;5;10m"
   yellow = "\u001b[48;5;11m"
   blue =   "\u001b[48;5;12m"
   purple = "\u001b[48;5;13m"
   cyan =   "\u001b[48;5;14m"
   white =  "\u001b[48;5;15m"


def LOG_ERROR(*text, sep=" ", end="\n"):
   print(fg.red    + bold + "[-] Error: "   + reset, end="")
   for i in text:
      print(i, end=sep)
   print(reset, end=end)
def LOG_WARNING(*text, sep=" ", end="\n"):
   print(fg.yellow    + bold + "[!] Warning: "   + reset, end="")
   for i in text:
      print(i, end=sep)
   print(reset, end=end)
def LOG_INFO(*text, sep=" ", end="\n"):
   print(fg.blue    + bold + "[?] Info: "   + reset, end="")
   for i in text:
      print(i, end=sep)
   print(reset, end=end)
def LOG_SUCCESS(*text, sep=" ", end="\n"):
   print(fg.green    + bold + "[-] Error: "   + reset, end="")
   for i in text:
      print(i, end=sep)
   print(reset, end=end)

def printl(arr:list, end="\n"):
   """
   printl joins a list, printing its items
   """
   for i in range(len(arr)):
      print(arr[i], end="")
   print(end=end)
def reset_color():
   """
   sets console color to initial state
   """
   print(reset, end="")
def set_color(*color:str):
   """
   sets console color to arg:'color'
   """
   for i in color:
      print(i, end="")
def format_color(*value, color:str) -> str:
   """
   returns a string formatted with arg:'color'
   """
   ret = reset+color
   for i in value:
      ret += i
   return ret