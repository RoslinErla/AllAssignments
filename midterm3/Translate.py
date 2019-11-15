# "Instant messaging" (IM) og "texting" á snjalltækjum hefur leitt af sér safn af algengum skammstöfunum sem er gagnlegt til að skrifa stutt skilaboð.  Skrifið Python forrit, translate.py, sem les einnar línu textaskilaboð, sem geta innihaldið algengar skammstafanir, og þýðir skilaboðin yfir á ensku með því að nota safn af þýðingapörum úr textaskrá. 

# Forritið á að lesa nafn á þýðingaskrá frá notanda og síðan leyfa notandanum að slá inn skammstöfuð skilaboð, endurtekið.  Fyrir sérhver skilaboð skal prenta út tilheyrandi þýðingu þangað til notandinn slær inn 'q'.

# ----

# Instant messaging (IM) and texting on smart devices has resulted in a collection of common abbreviations useful for brief messages.  Write a Python program, translate.py, that reads a one-line text message that may contain common abbreviations and translates the message into English, using a collection of tranlation pairs stored in a file.

# The program should prompt the user for the name of a translation (mapping) file and then repeatedly allow the user to enter (an abbreviated) message.  For each message, the corresponding translation is printed, until the user quits with a 'q'.

# ---

# Dæmi: Ef eftirfarandi þýðingaskrá, abbrev.txt, er gefin (sérhver lína inniheldur skammstafað orð/skilaboð, ásamt tvípunkti og tilheyrandi þýðingu):

# For example, given the following translations file, abbrev.txt: (each entry consists of an abbreviated word/message, followed by a colon and a translation):

# r:are
# y:why
# u:you
# ttyl:talk to you later
# l8:late
# ... þá er eftirfarandi inntak/úttak mögulegt:

# ... the following is a possible input/output sequence:


# Enter name of mapping file: abbrev.txt
# Enter a message: y r u l8?
# why are you late? 
# Enter a message: good to see u
# good to see you 
# Enter a message: ttyl
# talk to you later 
# Enter a message: u r l8!
# you are late! 
# Enter a message: q
# Athugið:

# ef þýðing finnst ekki fyrir tiltekið orð/skilaboð, þá skrifast orðið/skilaboðin út óbreytt.   
# ef greinarmerki er í enda orðs/skilaboða þá er það (aðeins eitt greinamerki) tekið burt áður en þýðing á sér stað og síðan sett aftur inn í enda þýdda orðsins/skilaboðanna.  
# Note:

# if a translation is not found for a given word/message, the word/message is written out unchanged.
# if a punctuation character is at the end of a word/message, it (only a single punctuation character) is stripped off before translation, and then put back onto the translated word/message.
# Ef þýðingaskráin finnst ekki þá skrifar forritið ekki neitt út.

# If the input mapping file is not found, the program does not generate any output.

# Enter name of mapping file: bla.txt
import string

def open_file():
    """Open the given file name and returns the file stream, or None if the file cannot be opened"""
    filename = input("Enter name of mapping file: ")
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None

def text_to_dict(file_stream):
    """Goes through the file and makes a dict of the abbreviations
       The abbreviation is the key the meaning the value"""
    abbrev_dict = dict()
    for lines in file_stream: #goes through it line to line
        if lines != "\n":
            lines = lines.strip()
            lines = lines.split(":")
            abbrev_dict[lines[0]] = lines[1:]
    return abbrev_dict


def messages(abbreviation, a_dict):
    """Reads the message, removes and adds punctuation and translates the message"""
    abbreviation = abbreviation.strip().split(" ")
    abbrev_list = list()
    
    for element in abbreviation:

        if element[-1] in string.punctuation: #Checks if there is any punctuation
            element_no_punct = element.replace(element[-1],"") #make a new variable not with the punction

            if element_no_punct not in a_dict: #Checks if the element - punct is in the dictionary
                abbrev_list.append(element) #If its not we just add the element
            
            else: # if it is in the dict we add the meaning of it to the dict. and add the punctuation back to it
                for key in a_dict:
                    if key == element_no_punct:
                        value_list = list(a_dict[key])
                        value_list.extend(element[-1])
                        value_list = "".join(value_list[0:])
                        abbrev_list.append(value_list)

        elif element not in a_dict: #If the element is not in the dict we add it as is 
            abbrev_list.append(element)
 
        else: #If the element is in the dict we add the meaning to it to the list
            for key in a_dict:
                if key == element:
                    abbrev_list.extend(a_dict[key])

    abbrev_list = " ".join(abbrev_list[0:])
    print(abbrev_list)

def main():
    file_stream = open_file()
    while file_stream: 
        abbrev_dict = text_to_dict(file_stream)
        abbrev = input("Enter a message: ")
        while abbrev != "q": #Stops asking for messages if you write "q"
            messages(abbrev,abbrev_dict)
            abbrev = input("Enter a message: ")
        else:
            file_stream = False


main()



