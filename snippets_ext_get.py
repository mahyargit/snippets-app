import sys
import argparse
import logging
import csv
import os.path

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)
 
def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
         writer = csv.writer(f)
         logging.debug("Writing snippet to file".format(name, snippet))
         writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet


def get(name, filename):
    """ Retrive a snippet with an associated name in the CSV file """
    logging.info("Reading {} from {}".format(name, filename))
    logging.debug("Opening file")


    with open(filename, "r") as f:
         reader = csv.reader(f)
         for row in reader:
                logging.debug("Reading snippet to file".format(name))
            	if name in row[0]: 
            		snippet = row[1]
                else:
                	 snippet = ("no item found" ) 
    return snippet


 
def make_parser():
     """ Construct the command line parser """
     logging.info("Constructing parser")
     description = "Store and retrieve snippets of text"
     parser = argparse.ArgumentParser(description=description)
 
     subparsers = parser.add_subparsers(help="Available commands")
 
# Subparser for the put command
     logging.debug("Constructing put subparser")
     put_parser = subparsers.add_parser("put", help="Store a snippet")
     put_parser.add_argument("name", help="The name of the snippet")
     put_parser.add_argument("snippet", help="The snippet text")
     put_parser.add_argument("filename", default="snippets.csv", nargs="?",
     help="The snippet filename")
     put_parser.set_defaults(command="put")

# Subparser for the get command
     logging.debug("Constructing get subparser")
     get_parser = subparsers.add_parser("get", help="Retrive a snippet")
     get_parser.add_argument("name", help="The name of the snippet")
     get_parser.add_argument("filename", default="snippets.csv", nargs="?",
     help="The snippet filename")
     get_parser.set_defaults(command="get")    
 
     return parser
 
def main():
     """ Main function """
     logging.info("Starting snippets")
     parser = make_parser()
     arguments = parser.parse_args(sys.argv[1:])
     # Convert parsed arguments from Namespace to dictionary
     arguments = vars(arguments)
     command = arguments.pop("command")
     
     if command == "put":
         name, snippet = put(**arguments)
         print "Stored '{}' as '{}'".format(snippet, name)
          
     if command == "get" and os.path.isfile(arguments["filename"]):
         name = get(**arguments)
         print "Retrive '{}' ".format(name)
     else:
         print " That File does not exist.."    

if __name__ == "__main__":
     main()