import logging, sys
logging_enabled = False
old_input = input
old_print = print
old_stderr = sys.stderr.write
def stderr_write(string=""):
    old_stderr(string)
    if logging_enabled:
        logging.error(string)
sys.stderr.write = stderr_write
def input(string=""):
    string_in = old_input(string)
    if logging_enabled:
        logging.info("STRING IN " + string_in)
    return string_in
logging.basicConfig(level=logging.DEBUG, filename='./OUT.txt') ### Print does not get overridden for some reason and sys.stdout.write needs redirecting. Perhaps redirect print function to sys.stdout.write func call with "\n" (or whatever sep) chosen. Also need to account for file being supplied :face_in_hands:
def print(string="", string2="", sep=" ", end="\n", file=sys.stdout, flush=False):
    # type: (string, string, string, string, file_object, boolean) -> None
    old_print(string, string2, sep = sep, end=end, file=file, flush=flush)
    if logging_enabled:
        logging.info(string)
        logging.info(string2)
