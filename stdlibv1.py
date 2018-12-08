import logging, sys
debug = input("Debug or not")
if debug == "1":
    old_input = input
    sys.stderr.write = logging.info
    def input(string=""):
        string_in = old_input(string)
        logging.info("STRING IN " + string_in)
        return string_in
    logging.basicConfig(level=logging.DEBUG, filename='./OUT.txt')
    old_print = print
    def print(string="", string2=""):
        old_print(string, string2)
        logging.info(string)
        logging.info(string2)
print("OMG")
b = input()
print(a) ## Deliberate error for testing
