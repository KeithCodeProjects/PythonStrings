#Keith Hicks
#CIT 253
#Final Programming

# This program allows a user to select/open a file and perform different options on the file such as
# count number of times a single word appears in the file, print all lines to new file containing that word,
# count number of times a string appears in the file, print all lines to new file containing that string,
# and enter a string and a substitution for that string to replace everywhere it appears in the file and
# print the entire file containing the substitutions to a new file.


from tkinter import filedialog
from tkinter import *
import random
import os
from random import randrange
import re



class PythonString :

    def __init__(self):
       self.text =  []
       self.filename = ""
       self.infile = ""
       
# Using Tk open file dialog allowing user to select file to open.

    def openFile(self):
       root = Tk()
       root.withdraw()
       self.filename =  filedialog.askopenfilename(initialdir = "/",
                                            title = "Select file",
                                            filetypes = (("txt files","*.txt"),("all files","*.*"))) 
       
# Opens selected file, reads all lines into a list.

    def readFile(self, text):
        infile = open(self.filename, "r")

        try:
           for line in infile.readlines():
               line = line.strip()
               text.append(line)
        except:
           print(filename + " can not be processed")
        finally:
           infile.close()

        return text
    
        
#Uses regular expression to find a single word in the file and return count of number of times it appears.
#Takes the word to count and the list as arguments.
    
    def countWord(self, word, text):
        
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), str(text), flags = re.IGNORECASE))
                
        return count
        
#Uses regular expression to find a single word in the file and print all lines the word occurs in to new file. 
#Takes the word to find and the list as arguments. Returns filename of new file created.  
    
    def searchLine(self, word, text):
        lines = []
        
        for line in text:
            if re.search(r'\b%s\S*\b' % re.escape(word), str(line), flags = re.IGNORECASE):
               line = line.strip()
               lines.append(line + "\n")
        outfile = open(self.checkfile(self.filename), "w")
        outfile.writelines(lines)
        outfile.close()
        return outfile.name
        
               
#Checks name of current file and if it exists in current directory.  If it doesn't exist saves the file with its current file name,
# if not increments and adds a number to end of file name as to not overwrite previous file. Takes the filename as argument.
#Uses import os library.

    def checkfile(self, filename):
        filename = os.path.expanduser(filename)

        if not os.path.exists(filename):
           return path
        index = 0
        root, ext = os.path.splitext(os.path.expanduser(filename))
        dir = os.path.dirname(root)
        fname = os.path.basename(root)
        cFile = fname + ext        
        lsd = set(os.listdir(dir))
        
        while cFile in lsd:
                cFile = "{}_{}{}".format(fname,index,ext)
                index    += 1
        return os.path.join(dir,cFile)
        
#Finds and returns count of number of times string appears in file.  Takes the string to find and list as arguments.
    
    def countString(self, word, text):

        count = sum(1 for _ in re.finditer(r'\s*%s\S*\s*' % re.escape(word), str(text), flags = re.IGNORECASE))
                
        return count

#Finds string in file and prints all lines containing the string to new file.  Returns file name of new file.
#Takes the string to find and list as arguments.
    
    def searchLineString(self, word, text):
        lines = []
        
        for line in text:
            if re.search(r'\s*%s\S*\s*' % re.escape(word), str(line), flags = re.IGNORECASE):
               line = line.strip()
               lines.append(line + '\n')
        outfile = open(self.checkfile(self.filename), "w")
        outfile.writelines(lines)
        outfile.close()
        return outfile.name
        

#Finds a string and replaces it with substitution everywhere the string occurrs in the file.
#Prints the whole file with substitution string in place of the string to new file.  Returns new file name.
#Takes the string to find, substitution string and list as arguments.
    
    def subString(self, word, repWord, text):
        lines = []
        newLines = []

        for line in text:
            a = re.sub(r'\b%s\S*\b' % word, repWord, str(line), flags = re.IGNORECASE) 
            line = line.strip()
            lines.append(a + '\n')
       
        outfile = open(self.checkfile(self.filename), "w")
        outfile.writelines(lines)
        outfile.close()
        return outfile.name


#Creates a menu of all selections for the user and runs the program.
    
    def run(self):
        
                   
        running = True
        while running:
            print("Select a file to open\n")
            n = 1
            self.openFile()
            lines = []
            self.readFile(lines)
            
                  
            done = False
            while not done:
                print("Select an option")
                print("\n1. Open File new file")
                print("2. Count a single word")
                print("3. Print lines to new file containing a word")
                print("4. Count a string")
                print("5. Print lines to new file containing string")
                print("6. Substitute a string and print to new file")
                print("7. Exit")
                selection = input()
            
            
                if  selection == "1" :
                      done = True
                elif selection == "2" :
                      print("Enter a word to count\n")
                      word = input()
                      print(word + " was found " + str(self.countWord(word, lines)) + " times\n")
                elif selection == "3" :
                      print("Enter a word to print all lines containing it to new file\n")
                      word = input()
                      print("The name of the new file containing " + word + " is " + self.searchLine(word, lines) + "\n")
                elif selection == "4":
                      print("Enter a string to count")
                      word = input()
                      print(word + " was found " + str(self.countString(word, lines)) + " times\n")
                elif selection == "5" :
                      print("Enter a string to print all lines containing it to new file\n")
                      string = input()
                      print("The name of the new file containing " + string + " is " + self.searchLineString(string, lines) + "\n")
                elif selection == "6" :
                      print("Enter a string to find\n")
                      string = input()
                      print("Enter a string to substitute for previous entry\n")
                      sub = input()
                      print("The name of the new file containing " + string + " replaced with " +
                            sub + " is " + self.subString(string, sub, lines) + "\n")
                elif selection == "7" :
                      done = True
                      running = False
                      
                      
                

#Main
def main():
    new = PythonString()
    new.run()

main()

    



    


