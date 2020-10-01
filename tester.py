from logger import log

# print(REVERSED + "Hola" + RESET)
# print(BOLD + "Hola")
# print(UNDERLINE + "Hola" + RESET)

log.ERROR("An Error Occurred Unexpectedly")
log.WARNING("Something strange is happening")
log.SUCCESS("Everything is working fine")
log.INFO("Something is working...")

#print(RESET + BACK_BLUE + "Some Text")
print(log.reset)


# example API usage

# log.INFO("some text") #prints "[?] INFO: some text" with colors
# log.enable_save_to_txt("C:/SomeFolder") #stars saving following logs to txt into path, if empty saves to class position
# log.WARNING("something's happening") #prints "[!] WARNING: something's happening" with colors both to cmd and to txt
# log.enable_date_timestamp("dd/mm/yy") #starts printing text with date timestamp with the given format (default = "dd/mm/yy")
# log.enable_time_timestamp("hh:mm:ss") #stars printing text with time timestamp  with the given format (default = "hh:mm:ss")
# log.disable_colors()
# log.enable_colors()

# stuff to test: template method, strategy, classes/inheritance, composition, many little classes combined into one

# implementing your own logger

from logger import log_context, custom_logger


class MyLogger(custom_logger.MiniLog):
    def log(self, text):
        print(text)


log_context.set_logger(MyLogger())

log_context.log("text")