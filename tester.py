from logger import *

# print(REVERSED + "Hola" + RESET)
# print(BOLD + "Hola")
# print(UNDERLINE + "Hola" + RESET)
set_color(bg.white, fg.black)
print("PYTHON LOGGER BY COGNO-MARCO & CARPAL")
reset_color()

LOG_ERROR(fg.cyan,"An Error Occurred Unexpectedly")
LOG_WARNING(fg.cyan,"Something strange is happening")
LOG_SUCCESS(fg.cyan,"Everything is working fine")
LOG_INFO(fg.cyan,"Something is working...", end="\n\n")

string = [
   fg.green,
   "I",
   fg.white,
   "T",
   fg.red,
   "A",
   "\n",
   reset
]
printl(string) # print array
print(url+"https://github.com/Cogno-Marco/YetAnotherPyLogger",
   format_color("->", color=fg.red),
   format_color("Star ", color=fg.yellow)
)
reset_color() # reset colors