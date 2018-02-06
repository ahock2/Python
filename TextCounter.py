# File: TextCounter.py

"""
Name: TextCounter.py

Creater: Adam Hock

Date started: 1/27/2018

Description:    This program can open up a user's text file, read it, and give a count
                of how many words, lines, paragraphs, and sentences there are in the
                text file. This program does not work for Word Document (.docx) files.
                If you want to try my program with a Word Document file, you can save
                your Word Document as a Plain Text file (.txt)

Comments:       This program only took me a couple of hours on a Saturday to write. It
                was initially supposed to be only a word counter, but I made additional
                functions as I went along. Going forward, I would like to edit this
                program to make it read Word Document files and broaden the scope of which
                this program can give accurate data (For example, this program inaccurately
                lists the number of sentences in your program if the last line of your
                program is blank)
                
                Warning! This sentence counter part of the code does not take initials into consideration
                (example: "The book was written by A. J. Hock." will count as 3 sentences in the sentence counter
                if there is a space preceding the period. "The book was written by A.J. Hock" will count as 2 sentences.
        
        
"""

def ReadFile(text, filename):
        """
        This function reads the title and the contents of
        the file the user has selected. This is to ensure
        that the user has picked the correct file.
        """
        
        print("\nThis is the file you've selected\n")
        print(filename)
        print("\nThis is what your file says\n")
        print(text)

def WordCount(text):
        """
        This function outputs the number of words in the
        text file chosen by the user.

        It does this by splitting the text file into each
        individual line. Then in splits each line into
        individual words. Lastly, it omits spaces at the
        end of lines. It counts each word per line for
        every line, and outputs the count at the end.
        """
        num_lines = text.split("\n")
        wordcount = 0
        for i in range(len(num_lines)):
                if num_lines[i]:
                        words = num_lines[i].split(" ")
                        for j in range(len(words)):
                                if words[j] == '':
                                        wordcount-=1
                        wordcount += len(words)
        print("\nThis is the word count of your text file\n")
        print(wordcount)

def LineCount(text):
        """
        This function counts the number of lines in the text
        file (including empty lines)
        """
        num_lines = 1+sum(1 for line in text if line == "\n")
        print("\nThis is the number of lines in your text file\n")
        print(num_lines)

def ParagraphCount(text):
        """
        This function counts the number of "Paragraphs" in the text.
        A paragraph is a group of lines separated from the rest of the text
        by two or more new lines like so.

        Paragraph 1
        Still Paragraph 1

        Paragraph 2



        Paragraph 3
        """
        text = text.split("\n")
        new_paragraphs = 1 + sum(1 for i in range(len(text)-1) if not text[i] and text[i+1])
        print("\nThis is the number of paragraphs (blocks of lines separated by multiple new lines) in your text file\n")
        print(new_paragraphs)

def SentenceCount(text):
        """
        This function counts every isolated period, exclamation point, and question mark.
        This is to prevent counting multiple sentences for lines such as this

        OMG!!! I won first place!?!
        I'm truly shocked...
        """
        sentence = 1 + text.count(". ") + text.count("! ") + text.count("? ") + text.count(".\n") + text.count("!\n") + text.count("?\n")
        print("\nThis is the number of sentences in your text file\n")
        print(sentence)

while True:
        #This loop iterates unless the user types choice 7
        filename = input("Enter a file name: ")
        with open(filename) as f:
                text = f.read()
        while True:
                #This loop iterates unless the user types choice 1 or 7
                print("\nPick one of the following options: \n")
                print("1. Enter a new file")
                print("2. Read the file")
                print("3. Word Count")
                print("4. Line Count")
                print("5. Paragraph Count")
                print("6. Sentence Count")
                print("7. Quit")
                choice = input("Choose your option's number: ")
                if choice == '1':
                        break
                elif choice == '2':
                        ReadFile(text, filename)
                elif choice == '3':
                        WordCount(text)
                elif choice == '4':
                        LineCount(text)
                elif choice == '5':
                        ParagraphCount(text)
                elif choice == '6':
                        SentenceCount(text)
                elif choice == '7':
                        break
                else:
                        print("\nInvalid Input!\n")
                        continue
        if choice == '7':
                break
        else:
                continue
f.close()
                
